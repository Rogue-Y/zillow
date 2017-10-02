# from .test_config import test_config
from .config_linear import config_linear
from .config_lightgbm import config_lightgbm, config_lightgbm_new
from .config_xgboost import config_xgboost, config_xgboost_new
from .config_ensembles import config_rf, config_extra_tree, config_gb
from .config_gaussian_process import config_gaussian_process


# stacking configurations
from .stacking_config_test import stacking_config_test
