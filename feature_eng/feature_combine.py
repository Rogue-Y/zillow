# Combine features
import os
import inspect

import pandas as pd

import utils
import feature_eng

FEATURE_PICKLE_FOLDER = 'features/'

def list_features():
    # Iterate through functions to generate a feature list
    feature_list = []
    functions = inspect.getmembers(feature_eng, lambda x: callable(x))
    for name, function in functions:
        name_lower = name.lower()
        if 'bin' in name_lower or 'encode' in name_lower or 'cross' in name_lower:
            continue
        feature_list.append(name)
    with open('feature_list.txt', 'w') as feature_list_handler:
        for function_name in feature_list:
            feature_list_handler.write(
                "('%s', %s, {}, '%s'),\n"
                % (function_name,
                    '.'.join(['feature_eng', function_name]),
                    function_name+'_pickle'))

# each feature in the feature_list is a tuple in the form (name, method, pickle_path)
def feature_combine(df, feature_list, force_generate=False):
    features = []
    for name, generator, kwparams, pickle_path in feature_list:
        pickle_path = FEATURE_PICKLE_FOLDER + pickle_path
        if not force_generate and os.path.exists(pickle_path):
            feature = pd.read_pickle(pickle_path)
        else:
            print(pickle_path)
            feature = generator(df, **kwparams)
            feature.to_pickle(pickle_path)
        features.append(features)
    for feature in features
    return pd.concat(features, axis=1, ignore_index=True)

if __name__ == "__main__":
    feature_list = [
        ('average_room_size', feature_eng.average_room_size, {}, 'average_room_size_pickle'),
        ('boolean_has_ac', feature_eng.boolean_has_ac, {}, 'boolean_has_ac_pickle'),
        ('boolean_has_garage_pool_or_ac', feature_eng.boolean_has_garage_pool_or_ac, {}, 'boolean_has_garage_pool_or_ac_pickle'),
        ('boolean_has_heat', feature_eng.boolean_has_heat, {}, 'boolean_has_heat_pickle'),
        ('building_age', feature_eng.building_age, {}, 'building_age_pickle'),
        ('built_before_year', feature_eng.built_before_year, {}, 'built_before_year_pickle'),
        ('category_ac_type_one_hot', feature_eng.category_ac_type_one_hot, {}, 'category_ac_type_one_hot_pickle'),
        ('category_fips_type_one_hot', feature_eng.category_fips_type_one_hot, {}, 'category_fips_type_one_hot_pickle'),
        ('category_heating_type_one_hot', feature_eng.category_heating_type_one_hot, {}, 'category_heating_type_one_hot_pickle'),
        ('category_land_use_code', feature_eng.category_land_use_code, {}, 'category_land_use_code_pickle'),
        ('category_land_use_code_one_hot', feature_eng.category_land_use_code_one_hot, {}, 'category_land_use_code_one_hot_pickle'),
        ('category_land_use_desc', feature_eng.category_land_use_desc, {}, 'category_land_use_desc_pickle'),
        ('category_land_use_desc_one_hot', feature_eng.category_land_use_desc_one_hot, {}, 'category_land_use_desc_one_hot_pickle'),
        ('category_land_use_type', feature_eng.category_land_use_type, {}, 'category_land_use_type_pickle'),
        ('category_land_use_type_one_hot', feature_eng.category_land_use_type_one_hot, {}, 'category_land_use_type_one_hot_pickle'),
        ('deviation_from_avg_structure_tax_value', feature_eng.deviation_from_avg_structure_tax_value, {}, 'deviation_from_avg_structure_tax_value_pickle'),
        ('error_rate_calculated_finished_living_sqft', feature_eng.error_rate_calculated_finished_living_sqft, {}, 'error_rate_calculated_finished_living_sqft_pickle'),
        ('extra_rooms', feature_eng.extra_rooms, {}, 'extra_rooms_pickle'),
        ('extra_space', feature_eng.extra_space, {}, 'extra_space_pickle'),
        ('geo_city_structure_tax_value', feature_eng.geo_city_structure_tax_value, {}, 'geo_city_structure_tax_value_pickle'),
        ('geo_city_tax_value', feature_eng.geo_city_tax_value, {}, 'geo_city_tax_value_pickle'),
        ('geo_lat_lon_block', feature_eng.geo_lat_lon_block, {}, 'geo_lat_lon_block_pickle'),
        ('geo_lat_lon_block_tax_value', feature_eng.geo_lat_lon_block_tax_value, {}, 'geo_lat_lon_block_tax_value_pickle'),
        ('geo_neighorhood_tax_value', feature_eng.geo_neighorhood_tax_value, {}, 'geo_neighorhood_tax_value_pickle'),
        ('geo_region_tax_value', feature_eng.geo_region_tax_value, {}, 'geo_region_tax_value_pickle'),
        ('geo_zip_tax_value', feature_eng.geo_zip_tax_value, {}, 'geo_zip_tax_value_pickle'),
        ('missing_value_count', feature_eng.missing_value_count, {}, 'missing_value_count_pickle'),
        ('missing_value_one_hot', feature_eng.missing_value_one_hot, {}, 'missing_value_one_hot_pickle'),
        ('multiply_lat_lon', feature_eng.multiply_lat_lon, {}, 'multiply_lat_lon_pickle'),
        ('poly_2_structure_tax_value', feature_eng.poly_2_structure_tax_value, {}, 'poly_2_structure_tax_value_pickle'),
        ('poly_3_structure_tax_value', feature_eng.poly_3_structure_tax_value, {}, 'poly_3_structure_tax_value_pickle'),
        ('ratio_living_area', feature_eng.ratio_living_area, {}, 'ratio_living_area_pickle'),
        ('ratio_structure_tax_value_to_land_tax_value', feature_eng.ratio_structure_tax_value_to_land_tax_value, {}, 'ratio_structure_tax_value_to_land_tax_value_pickle'),
        ('ratio_tax', feature_eng.ratio_tax, {}, 'ratio_tax_pickle'),
        ('round_lat', feature_eng.round_lat, {}, 'round_lat_pickle'),
        ('round_lon', feature_eng.round_lon, {}, 'round_lon_pickle'),
        ('round_multiply_lat_lon', feature_eng.round_multiply_lat_lon, {}, 'round_multiply_lat_lon_pickle'),
        ('sum_lat_lon', feature_eng.sum_lat_lon, {}, 'sum_lat_lon_pickle'),
        ('total_rooms', feature_eng.total_rooms, {}, 'total_rooms_pickle')
    ]
    prop = utils.load_properties_data(data_folder='../data/')
    features = feature_combine(prop, feature_list)
    print(features.shape)
    features.to_csv('test_feature_combine.csv')
