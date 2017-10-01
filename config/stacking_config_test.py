from models import Lightgbm
from .config_linear import config_linear
from .lightgbm_config import lightgbm_config
from hyperopt import hp

stacking_config_test = {
    'name': 'stacking_config_test',
    'stacking_list': [
        (config_linear, False),
        (lightgbm_config, False),
    ],
    'Meta_model': Lightgbm.Lightgbm,
    # predicting parameters
    'model_params': None,
    # 'resale_offset': 0.012,

    # tuning parameters
    'tuning_params': {
        'parameter_space': {
            'model_params': {
                'learning_rate': hp.loguniform('learning_rate', -2, 0),
                'boosting_type': 'gbdt',
                'objective': 'regression',
                'metric': hp.choice('metric', ['mae', 'mse']),
                # 'sub_feature': hp.uniform('sub_feature', 0.1, 0.5),
                'num_leaves': hp.choice('num_leaves', list(range(10, 151, 15))),
                'min_data': hp.choice('min_data', list(range(150, 301, 15))),
                'min_hessian': hp.loguniform('min_hessian', -3, 1),
                'num_boost_round': hp.choice('num_boost_round', [200, 300, 500]),
                'max_bin': hp.choice('max_bin', list(range(50, 151, 10))),
                # 'bagging_fraction': hp.uniform('bagging_fraction', 0.5, 1),
                # 'bagging_freq': hp.choice('bagging_freq', list(range(0, 100, 10))),
                'verbose': -1
            },
        },
        'max_evals': 2,
    }
}