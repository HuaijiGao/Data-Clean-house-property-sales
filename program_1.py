from header import read_data, VALID_REGION_NAMES, VALID_COUNCIL_AREAS
from pprint import pprint  # Only used for test purpose


def clean_sales_data(data):
    """
    This function is to duplicate the input data, clean the realestate 
    information and return.
    
    Args:
        data (dict): a dictionary in the format returned by read_data.
    
    Returns:
        clean_data (dict): a duplicated cleaned dictionary of the input data.
    """
    clean_data = dict_deep_copy(data)
    to_be_cleaned = ["Price", "Regionname", "SaleDate", "Postcode", \
                     "CouncilArea"]
    # For each realestate record, clean the data of those categories in
    # to_be_cleaned.
    for realestate in clean_data.values():
        for info in to_be_cleaned:
            realestate[info] = data_cleaning(info, realestate[info])
    return clean_data


def dict_deep_copy(data):
    """
    This function is to make deep copy of a nested dictionary.
    
    Args:
        data (dict): a nested dictionary.
        
    Returns:
        data_copy (dict): a deep copied dictionary of data.
    """
    data_copy = {}
    for key1 in data:
        data_copy[key1] = {}
        for key2, value2 in data[key1].items():
            data_copy[key1][key2] = value2
    return data_copy


def data_cleaning(info, val): 
    """
    This function is to validate "val" based on the following associated rules 
    of each "info".
    
    Args:
        info (str): valid key in the dictionary of realestate information data, 
          those valid key are stored in TO_BE_CLEANED.
        val (str): the value in the dictionary of realestate information data.
    
    Returns:
        None (NoneType): if val is invalid; or
        council (str): if info is "CouncilArea", val pass the partial matching
          and set similarity test; or
        val (str): for the remaining cases.
    """
    VALID_DAYS = {"2016": {"01": 31, "02": 29, "03": 31, "04": 30, 
                           "05": 31, "06": 30, "07": 31, "08": 31, 
                           "09": 30, "10": 31, "11": 30, "12": 31},
                  "2017": {"01": 31, "02": 28, "03": 31, "04": 30, 
                           "05": 31, "06": 30, "07": 31, "08": 31, 
                           "09": 30, "10": 31, "11": 30, "12": 31}}
    
    # The Price value cannot be non-numeric.
    if info == "Price":
        if val.isdigit():
            return val
        return None

    # The Regionname name should be in list VALID_REGION_NAMES.
    if info == "Regionname":
        if val in VALID_REGION_NAMES:
            return val
        return None
    
    # The SaleDate should be valid dates of year 2016 and 2017.
    if info == "SaleDate":
        if "/" in val and len(val.split("/")) == 3:
            day, month, year = val.split("/")
            if year in VALID_DAYS and \
               month in VALID_DAYS[year] and \
               1 <= int(day) <= VALID_DAYS[year][month]:
                return val
        return None
    
    # The Postcode should be valid Victoria's postcode (3000 - 3999).
    if info == "Postcode":
        if val.isdigit() and 3000 <= int(val) <= 3999:
            return val
        return None

    # The CouncilArea should be either in VALID_COUNCIL_AREAS or be the
    # most similar council area (based on set similarity test). 
    if info == "CouncilArea":
        if val in VALID_COUNCIL_AREAS:
            return val
        sim_max = 0
        council = None
        for valid_council in VALID_COUNCIL_AREAS:
            sim = set_similarity(val, valid_council)
            if sim > sim_max:
                sim_max = sim
                council = valid_council
            elif sim == sim_max:
                council = None
        return council
      
        
def set_similarity(s1, s2):
    """
    This function is to measure the set similarity of two strings 
    (not case sensitive). 
    
    Args:
        s1 (str): a character string.
        s2 (str): a character string.
    
    Returns:
        sim (float): a set similarity score.
    """
    set1 = set(s1.lower())
    set2 = set(s2.lower())
    sim = len(set1 & set2) / len(set1 | set2)
    return sim


# to test your function with 'noisy_data.csv' or another CSV file,
# change the value of this variable
test_file = 'sales_data_noisy_sample.csv'

# you don't need to modify the code below
if __name__ == '__main__':
    data_noisy = read_data(test_file)
    pprint(clean_sales_data(data_noisy))
