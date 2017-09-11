# Ensembling prediction result
# TODO(hzn):
#   *1. how to record ensembling experiements result
#   *2. how to envaluate ensembling in cv rather than submit the result, predictions
#       actually contains the training houses
#   *3. following the above one, how to automatically tune ensembling
#   *3. adjust for resale first or ensembling first (mathematically the same,
#       but the adjust offset could be different for different ensembling, also
#       the adjustment may affect validation, validation should be made with
#       pre-adjusted predictions)

import datetime
import gc
import time
from optparse import OptionParser

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

from config import test_config, lightgbm_config
from evaluator import Evaluator
from features import utils, data_clean
from models import Lightgbm
from train import prepare_features, prepare_training_data

# tuples of format (pickle_path, weight)
prediction_list = [
    ('XGBoost_latest_pickle', 7),
    # ('Lightgbm_latest_pickle', 3)
]

def ensemble(prediction_list=prediction_list):
    print('Ensembling...')
    print('loading sample submission...')
    df_test, sample = utils.load_test_data()
    # ensembling
    print('ensembling...')
    # initialize the prediction with bias, currently 0
    pred_sum = np.zeros(sample.shape[0])
    total_weight = 0
    for pickle_path, weight in prediction_list:
        pred = pd.read_pickle('data/predictions/%s' %pickle_path)
        pred = weight * pred.as_matrix()
        total_weight += weight
        pred_sum += pred
    ensembled_pred = pred_sum / total_weight

    # generate submission
    print("generating submission...")
    for c in sample.columns[sample.columns != 'ParcelId']:
        # sample[c] = avg_pred
        sample[c] = ensembled_pred
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sample.to_csv(
        'data/submissions/Submission_%s.csv' %time, index=False, float_format='%.4f')

# first layer of stacking
stacking_list = [
    test_config,
    lightgbm_config
]

meta_model = Lightgbm.Lightgbm()

FOLDS= 5

def stacking(stacking_list=stacking_list, meta_model=meta_model):
    print('Stacking...')

    kf = KFold(n_splits=FOLDS, shuffle=True, random_state=42)

    first_layer_preds = []

    for config_dict in stacking_list:
        # Read config
        # Mandatory configurations:
        # Feature list
        feature_list = config_dict['feature_list']
        # model
        Model = config_dict['model']

        # Optional configurations:
        # model params:
        model_params = config_dict['model_params'] if 'model_params' in config_dict else None
        # if record training
        record = config_dict['record'] if 'record' in config_dict else False
        # if generate submission or not
        submit = config_dict['submit'] if 'submit' in config_dict else False
        # outliers removal upper and lower percentile
        outliers_up_pct = config_dict['outliers_up_pct'] if 'outliers_up_pct' in config_dict else 99
        outliers_lw_pct = config_dict['outliers_lw_pct'] if 'outliers_lw_pct' in config_dict else 1
        # resale offset
        resale_offset = config_dict['resale_offset'] if 'resale_offset' in config_dict else 0.012
        # clean_na
        clean_na = config_dict['clean_na'] if 'clean_na' in config_dict else False
        # PCA component
        pca_components = config_dict['pca_components'] if 'pca_components' in config_dict else -1
        # PCA cannot deal with infinite numbers
        if pca_components > 0:
            clean_na = True

        prop = prepare_features(feature_list)
        train_df, transactions = prepare_training_data(prop, clean_na)
        del transactions; del prop; gc.collect()

        X_y = data_clean.drop_training_only_column(train_df)
        X, y = utils.get_features_target(X_y)

        model = Model(model_params = model_params)
        preds = []

        for train_index, validate_index in kf.split(X):     
            X_train, y_train = X.loc[train_index], y.loc[train_index]
            X_validate, y_validate = X.loc[validate_index], y.loc[validate_index]

            # try remove outliers
            print(X_train.shape, y_train.shape)
            ulimit = np.percentile(y_train.values, outliers_up_pct)
            llimit = np.percentile(y_train.values, outliers_lw_pct)
            mask = (y_train >= llimit) & (y_train <= ulimit)
            print(llimit, ulimit)
            X_train = X_train[mask]
            y_train = y_train[mask]

            # Training and predicting
            print('training...')
            model.fit(X_train, y_train)
            preds.append(
                pd.Series(model.predict(X_validate), index=validate_index))

        first_layer_preds.append(pd.concat(preds).sort_index())

    # assemble first layer result
    first_layer = pd.concat(first_layer_preds, axis=1)

    transactions = utils.load_transaction_data()
    _, y = utils.get_features_target(transactions)
    del transactions, _; gc.collect()

    print('second layer...')
    mean_errors = []
    # same k fold split as above
    # (this is guaranteed as long as the random seeds and the number of rows does not change,
    # therefore we only need to make sure the indexes of the dataframes are always aligned)
    for train_index, validate_index in kf.split(first_layer):     
        X_train, y_train = first_layer.loc[train_index], y.loc[train_index]
        X_validate, y_validate = first_layer.loc[validate_index], y.loc[validate_index]

        print('training...')
        meta_model.fit(X_train, y_train)
        train_pred = meta_model.predict(X_train)
        print("fold train mean error: ", Evaluator.mean_error(train_pred, y_train))

        print('validating...')
        y_pred = meta_model.predict(X_validate)
        # TODO(hzn): add output training records
        mae = Evaluator.mean_error(y_pred, y_validate)
        mean_errors.append(mae)
        print("fold validation mean error: ", mae)

    avg_cv_errors = np.mean(mean_errors)
    print("average cross validation mean error", avg_cv_errors)
    return avg_cv_errors

# Main method
if __name__ == '__main__':
    t1 = time.time()
    # Get configuration
    # parser to parse cmd line option
    parser = OptionParser()
    # ensemble is true by default or when -e flag is present
    parser.add_option('-e', '--ensemble', action='store_true', dest='ensemble', default=True)
    # ensemble is set to false when -s flag is present
    parser.add_option('-s', '--stacking', action='store_false', dest='ensemble')
    # parse cmd line arguments
    (options, args) = parser.parse_args()

    if options.ensemble:
        ensemble()
    else:
        stacking()

    t2 = time.time()
    print((t2 - t1) / 60)
