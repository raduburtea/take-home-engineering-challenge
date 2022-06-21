__app_name__ = "find_nearest_restaurants"
__version__ = "0.1.0"

dataset_path = 'find_nearest_restaurants/Mobile_Food_Facility_Permit.csv'

(
    SUCCESS,
    K_NOT_INT,
    LATITUDE_OUT_OF_RANGE,
    LONGITUDE_OUT_OF_RANGE,
    COORDINATE_WRONG_FORMAT,
    MISSING_INPUT,
    K_LESS_0,
) = range(7)

ERRORS = {
    K_NOT_INT: "K has to be an integer",
    LATITUDE_OUT_OF_RANGE: "Value out of range for latitude",
    LONGITUDE_OUT_OF_RANGE: "Value out of range for longitude",
    COORDINATE_WRONG_FORMAT: "Wrong format for coordinates",
    MISSING_INPUT: 'Not enough input values',
    K_LESS_0: "K can not be less than or equal to 0"
}