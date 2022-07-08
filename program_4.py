from header import read_data
from pprint import pprint  # Only used for test purpose
from json import loads


def provide_realestate_info(main_data, queried_properties):
    """
    This function is to generate a list of records of queried properties from 
    the realestate information data.
    
    Args:
        main_data (dict): a dictionary of clean data returned by read_data.
        queried_properties (JSON): a JSON object containing the core address
          information (Suburb, Address, Postcode) for a set of properties.
    Returns:
        result (list): a list of JSON-style dictionary structures that stores 
        the detailed information of the queried properties.
    """
    units = loads(queried_properties)
    # Get records for each property, and remove "None" from the result.
    data_raw = [get_record(main_data, queried_unit) for queried_unit in units]
    result = [record for record in data_raw if record != None]
    return result


def get_record(data, queried_unit):
    """
    This function is to retrieve the record of a queried property.
    
    Args:
        data (dict): a dictionary storing the realestate information.
        queried_unit (dict): a dictionary containing the core address 
          information (Suburb, Address, Postcode) of a queried property.
    
    Returns:
        record (dict): a dictionary containing the detailed information 
          (Address, Bedrooms, Landsize, Postcode, Price, Suburb) of the
          queried property; or
        None (NoneType): if such a property could not be found.
    """
    count = 0
    record = None
    # Check if the Suburb and Postcode are matched. If so, check partial match 
    # for Address, if more than one property is found, return None because 
    # there is no way to decide which of the properties it is.
    for realestate in data.values():
        if queried_unit["Suburb"] == realestate["Suburb"] and \
           queried_unit["Address"] in realestate["Address"] and \
           str(queried_unit["Postcode"]) == realestate["Postcode"]:
            count += 1
            if count > 1:
                return None
            record = queried_unit.copy()
            record["Address"] = realestate["Address"]
            record["Price"] = int(realestate["Price"])
            record["Bedrooms"] = int(realestate["Bedrooms"])
            record["Landsize"] = int(realestate["Landsize"])       
    return record      


# Change these variables to test your function with another CSV file
# or with another test case
test_file = 'sales_data_clean.csv'
queried_properties_test = '[{"Suburb": "Rosanna", "Address": "7 Hylton Cr", "Postcode": 3084}, \
{"Suburb": "Preston", "Address": "3/152 Tyler St", "Postcode": 3072}, \
{"Suburb": "Epping", "Address": "19 Houston St", "Postcode": 3076}]'

# You don't need to modify the code below
if __name__ == '__main__':
    data_cleaned = read_data(test_file)
    pprint(provide_realestate_info(data_cleaned, queried_properties_test))
