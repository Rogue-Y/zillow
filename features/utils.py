import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import json
import os

# utility functions
def plot_score(y, y_hat):
    return (np.mean(abs(y-y_hat)))

def load_train_data(data_folder='data/', force_read=False):
    """ Load transaction data and properties data.
        Returns:
            (train_df, properties_df)
    """
    train = load_transaction_data(data_folder, force_read)
    prop = load_properties_data(data_folder, force_read)

    return (train, prop)

def load_transaction_data(data_folder='data/', force_read=False):
    """ Load transaction data.
        Returns:
            train_df
    """
    train_data_pickle = data_folder + 'train_2016_v2_pickle'

    if not force_read and os.path.exists(train_data_pickle):
        train = pd.read_pickle(train_data_pickle)
    else:
        train = pd.read_csv(
            data_folder + 'train_2016_v2.csv', parse_dates=['transactiondate'])
        train.to_pickle(train_data_pickle)
    return train

def load_properties_data(data_folder='data/', force_read=False):
    """ Load properties data.
        Returns:
            properties_df
    """
    prop_data_pickle = data_folder + 'properties_2016_pickle'

    if not force_read and os.path.exists(prop_data_pickle):
        prop = pd.read_pickle(prop_data_pickle)
    else:
        prop = pd.read_csv(data_folder + 'properties_2016.csv')
        # Convert float64 to float32 to save memory
        for col in prop.columns:
            if prop[col].dtype == 'float64':
                prop[col] = prop[col].astype('float32')
        prop.to_pickle(prop_data_pickle)
    return prop

def load_test_data(data_folder='data/', force_read=False):
    """ Load data and join trasaction data with properties data.
        Returns:
            (joined_test_df, sample_submission_df)
    """
    test_data_pickle = data_folder + 'sample_submission_pickle'
    if not force_read and os.path.exists(test_data_pickle):
        sample = pd.read_pickle(test_data_pickle)
    else:
        sample = pd.read_csv(data_folder + 'sample_submission.csv')
        sample.to_pickle(test_data_pickle)
    # sample submission use "ParcelId" instead of "parcelid"
    test = sample.rename(index=str, columns={'ParcelId': 'parcelid'})
    # drop the month columns in sample submission
    test.drop(['201610', '201611', '201612', '201710', '201711', '201712'],
        axis=1, inplace=True)
    return (test, sample)

def load_config(config_file='config/steps.json'):
    """ Read config file
        Returns: config JSON object
    """
    config_file = open(config_file, "r")
    config = None
    try:
        config = json.load(config_file)
    finally:
        config_file.close()
    return config


def train_valid_split(X, y, test_size):
    return train_test_split(X, y, test_size=test_size, random_state=42)

def get_features_target(df):
    """ Get features dataframe, and target column
        Call clean data and drop column in data_clean.py function before use
        this method.
        Returns:
            (X, y)
    """
    # logerror is the target column
    target = df['logerror']
    df.drop(['logerror'], axis=1, inplace=True)
    return (df, target)

def split_by_date(df, split_date = '2016-10-01'):
    """ Split the transaction data into two part, those before split_date as
        training set, those after as test set.
        Returns:
            (train_df, test_df)
    """
    df['transactiondate'] = pd.to_datetime(df['transactiondate'])
    # 82249 rows
    # loc is used here to get a real slice rather then a view, so there will not
    # be problem when trying to write to them.
    train_df = (df.loc[df['transactiondate'] < split_date, :]).reset_index(drop=True)
    # 8562 rows
    test_df = (df.loc[df['transactiondate'] >= split_date, :]).reset_index(drop=True)
    return (train_df, test_df)

def predict(predictor, train_cols):
    sample = pd.read_csv('sample_submission.csv')
    prop = pd.read_csv('properties_2016.csv')
    sample['parcelid'] = sample['ParcelId']
    df_test = sample.merge(prop, on='parcelid', how='left')
    x_test = df_test[train_cols]
    for c in x_test.dtypes[x_test.dtypes == object].index.values:
        x_test[c] = (x_test[c] == True)
    predictor.reset_parameter({"num_threads":1})
    p_test = predictor.predict(x_test)
    sub = pd.read_csv('sample_submission.csv')
    for c in sub.columns[sub.columns != 'ParcelId']:
        sub[c] = p_test

    sub.to_csv('lgb_starter.csv', index=False, float_format='%.4f')

def predict(predictor, X_test, sample, suffix=''):
    """ Predict on test set and write to a csv
        Params:
            predictor - the predictor, using lightgbm now
            X_test - the test features dataframe
            sample - sample_submission dataframe
            suffix - suffix of output file
    """
    predictor.reset_parameter({"num_threads":1})
    p_test = predictor.predict(X_test)
    for c in sample.columns[sample.columns != 'ParcelId']:
        sample[c] = p_test

    sample.to_csv('data/lgb_starter'+suffix+'.csv', index=False, float_format='%.4f')

# def get_train_test_sets():
#     """ Get the training and testing set: now split by 2016-10-01
#         transactions before this date serve as training data; those after as
#         test data.
#         Returns:
#             (X_train, y_train, X_test, y_test)
#     """
#     print('Loading data ...')
#     train, prop = load_train_data()
#
#     print('Cleaning data and feature engineering...')
#     prop_df = feature_eng.add_missing_value_count(prop)
#     prop_df = data_clean.clean_categorical_data(prop_df)
#
#     # Subset with transaction info
#     df = train.merge(prop_df, how='left', on='parcelid')
#     df = feature_eng.convert_year_build_to_age(df)
#     df = data_clean.drop_low_ratio_columns(df)
#     df = data_clean.clean_boolean_data(df)
#     df = data_clean.drop_id_column(df)
#     df = data_clean.fillna(df)
#
#     print("Spliting data into training and testing...")
#     train_df, test_df = split_by_date(df)
#     # 82249 rows
#     X_train, y_train = get_features_target(train_df)
#     # 8562 rows
#     X_test, y_test = get_features_target(test_df)
#
#     print("Done")
#     return (X_train, y_train, X_test, y_test)