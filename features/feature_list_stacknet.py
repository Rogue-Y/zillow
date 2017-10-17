feature_list_minimum = {
    'before_fill': [
        ('missing_value_count', 'missing_value_count', {}, 'missing_value_count_pickle', False),
    ],
    'original': [
        # required columns
        'parcelid',
        # optional columns
        'airconditioningtypeid',
        'architecturalstyletypeid',
        'basementsqft',
        'bathroomcnt',
        'bedroomcnt',
        'buildingclasstypeid',
        'buildingqualitytypeid',
        'calculatedbathnbr',
        'decktypeid',
        'finishedfloor1squarefeet',
        'calculatedfinishedsquarefeet',
        'finishedsquarefeet12',
        'finishedsquarefeet13',
        'finishedsquarefeet15',
        'finishedsquarefeet50',
        'finishedsquarefeet6',
        'fips',
        'fireplacecnt',
        'fullbathcnt',
        'garagecarcnt',
        'garagetotalsqft',
        'hashottuborspa',
        'heatingorsystemtypeid',
        'latitude',
        'longitude',
        'lotsizesquarefeet',
        'poolcnt',
        'poolsizesum',
        'pooltypeid10',
        'pooltypeid2',
        'pooltypeid7',
        'propertycountylandusecode',
        'propertylandusetypeid',
        'propertyzoningdesc',
        # 'rawcensustractandblock',
        'regionidcity',
        'regionidcounty',
        'regionidneighborhood',
        'regionidzip',
        'roomcnt',
        'storytypeid',
        'threequarterbathnbr',
        'typeconstructiontypeid',
        'unitcnt',
        'yardbuildingsqft17',
        'yardbuildingsqft26',
        'yearbuilt',
        'numberofstories',
        'fireplaceflag',
        'structuretaxvaluedollarcnt',
        'taxvaluedollarcnt',
        'assessmentyear',
        'landtaxvaluedollarcnt',
        'taxamount',
        'taxdelinquencyflag',
        'taxdelinquencyyear',
        'fips_census_1',
        'block_1',
        'fips_census_block',
        # 'censustractandblock',
    ],
    'generated': [
        # ('average_bathroom_size', 'average_bathroom_size', {}, 'average_bathroom_size_pickle', False),
        # ('average_bedroom_size', 'average_bedroom_size', {}, 'average_bedroom_size_pickle', False),
        # ('average_room_size', 'average_room_size', {}, 'average_room_size_pickle', False),
        # ('boolean_has_ac', 'boolean_has_ac', {}, 'boolean_has_ac_pickle', False),
        # ('boolean_has_garage_pool_and_ac', 'boolean_has_garage_pool_and_ac', {}, 'boolean_has_garage_pool_and_ac_pickle', False),
        # ('boolean_has_heat', 'boolean_has_heat', {}, 'boolean_has_heat_pickle', False),
        # ('building_age', 'building_age', {}, 'building_age_pickle', False),
        # ('built_before_year', 'built_before_year', {}, 'built_before_year_pickle', False),
        #
        # # # ('category_land_use_code', category_land_use_code, {}, 'category_land_use_code_pickle', False),
        # # ('category_land_use_code_encode', category_land_use_code_encode, {}, 'category_land_use_code_encode_pickle', False),
        # # # ('category_land_use_desc', category_land_use_desc, {}, 'category_land_use_desc_pickle', False),
        # # ('category_land_use_desc_encode', category_land_use_desc_encode, {}, 'category_land_use_desc_encode_pickle', False),
        # # ('category_land_use_type_encode', category_land_use_type_encode, {}, 'category_land_use_type_encode_pickle', False),
        #
        # ('error_rate_bathroom', 'error_rate_bathroom', {}, 'error_rate_bathroom_pickle', False),
        # ('error_rate_calculated_finished_living_sqft', 'error_rate_calculated_finished_living_sqft', {}, 'error_rate_calculated_finished_living_sqft_pickle', False),
        # ('error_rate_count_bathroom', 'error_rate_count_bathroom', {}, 'error_rate_count_bathroom_pickle', False),
        # ('error_rate_first_floor_living_sqft', 'error_rate_first_floor_living_sqft', {}, 'error_rate_first_floor_living_sqft_pickle', False),
        # ('extra_rooms', 'extra_rooms', {}, 'extra_rooms_pickle', False),
        # ('extra_space', 'extra_space', {}, 'extra_space_pickle', False),
        #
        # ('geo_city', 'geo_city', {}, 'geo_city_pickle', False),
        # ('geo_county', 'geo_county', {}, 'geo_county_pickle', False),
        # # ('geo_lat_lon_block_features', geo_lat_lon_block_features, {}, 'geo_lat_lon_block_features_pickle', False),
        # ('geo_fips_census_1', 'geo_fips_census_1', {}, 'geo_fips_census_1_pickle', False),
        # ('geo_fips_census_block', 'geo_fips_census_block', {}, 'geo_fips_census_block_pickle', False),
        # ('geo_neighborhood', 'geo_neighborhood', {}, 'geo_neighborhood_pickle', False),
        # ('geo_zip', 'geo_zip', {}, 'geo_zip_pickle', False),
        # ('multiply_lat_lon', 'multiply_lat_lon', {}, 'multiply_lat_lon_pickle', False),
        # ('poly_2_structure_tax_value', 'poly_2_structure_tax_value', {}, 'poly_2_structure_tax_value_pickle', False),
        # ('poly_3_structure_tax_value', 'poly_3_structure_tax_value', {}, 'poly_3_structure_tax_value_pickle', False),
        # ('ratio_basement', 'ratio_basement', {}, 'ratio_basement_pickle', False),
        # ('ratio_bedroom_bathroom', 'ratio_bedroom_bathroom', {}, 'ratio_bedroom_bathroom_pickle', False),
        # ('ratio_fireplace', 'ratio_fireplace', {}, 'ratio_fireplace_pickle', False),
        # ('ratio_floor_shape', 'ratio_floor_shape', {}, 'ratio_floor_shape_pickle', False),
        # ('ratio_living_area', 'ratio_living_area', {}, 'ratio_living_area_pickle', False),
        # ('ratio_living_area_2', 'ratio_living_area_2', {}, 'ratio_living_area_2_pickle', False),
        # ('ratio_pool_shed', 'ratio_pool_shed', {}, 'ratio_pool_shed_pickle', False),
        # ('ratio_pool_yard', 'ratio_pool_yard', {}, 'ratio_pool_yard_pickle', False),
        # ('ratio_structure_tax_value_to_land_tax_value', 'ratio_structure_tax_value_to_land_tax_value', {}, 'ratio_structure_tax_value_to_land_tax_value_pickle', False),
        # ('ratio_tax', 'ratio_tax', {}, 'ratio_tax_pickle', False),
        # ('ratio_tax_value_to_land_tax_value', 'ratio_tax_value_to_land_tax_value', {}, 'ratio_tax_value_to_land_tax_value_pickle', False),
        # ('ratio_tax_value_to_structure_value', 'ratio_tax_value_to_structure_value', {}, 'ratio_tax_value_to_structure_value_pickle', False),
        # ('round_lat', 'round_lat', {}, 'round_lat_pickle', False),
        # ('round_lon', 'round_lon', {}, 'round_lon_pickle', False),
        # # ('round_multiply_lat_lon', round_multiply_lat_lon, {}, 'round_multiply_lat_lon_pickle', False),
        # ('sum_lat_lon', 'sum_lat_lon', {}, 'sum_lat_lon_pickle', False),
        # ('total_rooms', 'total_rooms', {}, 'total_rooms_pickle', False),
        #
        # ('target_neighborhood_feature', 'target_region_feature', {'id_name':'regionidneighborhood'}, 'target_neighborhood_feature_pickle', False),
        # ('target_zip_feature', 'target_region_feature', {'id_name':'regionidzip'}, 'target_zip_feature_pickle', False),
        # ('target_city_feature', 'target_region_feature', {'id_name':'regionidcity'}, 'target_city_feature_pickle', False),
        # ('target_county_feature', 'target_region_feature', {'id_name':'regionidcounty'}, 'target_county_feature_pickle', False),
        # ('target_census_feature', 'target_region_feature', {'id_name':'fips_census_1'}, 'target_census_feature_pickle', False),
        # ('target_censusblock_feature', 'target_region_feature', {'id_name':'fips_census_block'}, 'target_censusblock_feature_pickle', False),

        # methods from feature clean_na
        # ('has_fireplace', 'has_fireplace', {}, 'has_fireplace_pickle', False),
        # ('is_garagetotalsqft_zero', 'is_garagetotalsqft_zero', {}, 'is_garagetotalsqft_zero_pickle', False),
        # ('has_partial_garagecarcnt', 'has_partial_garagecarcnt', {}, 'has_partial_garagecarcnt_pickle', False),
        # ('is_unitcnt_gt_four', 'is_unitcnt_gt_four', {}, 'is_unitcnt_gt_four_pickle', False),
        # ('has_shed_in_yard', 'has_shed_in_yard', {}, 'has_shed_in_yard_pickle', False),
        # ('is_numberofstories_gt_three', 'is_numberofstories_gt_three', {}, 'is_numberofstories_gt_three_pickle', False),
        # ('is_assessmentyear_2015', 'is_assessmentyear_2015', {}, 'is_assessmentyear_2015_pickle', False),
        # ('is_tax_assessed', 'is_tax_assessed', {}, 'is_tax_assessed_pickle', False),
        # ('is_taxdelinquencyyear_before_2014', 'is_taxdelinquencyyear_before_2014', {}, 'is_taxdelinquencyyear_before_2014_pickle', False),
        # ('tax_difference', 'tax_difference', {}, 'tax_difference_pickle', False),
        # ('has_construction_type', 'has_construction_type', {}, 'has_construction_type_pickle', False),
        # ('is_roomcnt_zero', 'is_roomcnt_zero', {}, 'is_roomcnt_zero_pickle', False),
    ]
}
