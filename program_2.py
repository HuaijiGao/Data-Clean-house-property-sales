from header import read_data, VALID_COUNCIL_AREAS
from pprint import pprint  # Only used for test purpose
from datetime import datetime


def sale_stats_by_council(data, start_date, end_date):
    """
    This function is to generate the sales statistics for each council area 
    in a given time frame (from start_date to end_date).
    
    Args:
        data (dict): a dictionary of clean data returned by read_data.
        start_date (str): a string with format dd/mm/yyyy.
        end_date (str): a string with format dd/mm/yyyy. 
    
    Returns:
        -1 (int): if start_date is greater than end_date; or
        stats (dict): a dictionary of statistic summary if start_date is not 
          greater than end_dat.
    """
    # Assume date inputs are valid (format: "dd/mm/yyyy")
    # check if the start date is greater than the end date.
    date_first = datetime.strptime(start_date, "%d/%m/%Y")
    date_last = datetime.strptime(end_date, "%d/%m/%Y")
    if date_first > date_last:
        return -1
    
    # Create a dictionary to store the result. For each council area, create 
    # an empty list to store valid sale prices.
    stats = {}
    for council in VALID_COUNCIL_AREAS:
        stats[council] = []
    
    # If SaleDate and Price are valid, store that price to the list of each
    # CouncilArea.
    for value in data.values():
        if value["SaleDate"] != None and value["Price"] != None:
            date = datetime.strptime(value["SaleDate"], "%d/%m/%Y")
            if date_first <= date <= date_last:
                stats[value["CouncilArea"]].append(int(value["Price"]))
    
    # If the list of prices is not empty, calculate the statistics, otherwise
    # assign None to the statistics.
    for council in VALID_COUNCIL_AREAS:
        prices = stats[council]
        if prices:
            stats[council] = {"avg": round(sum(prices) / len(prices)),
                              "max": max(prices),
                              "min": min(prices),
                              "sum": sum(prices)}
        else:
            stats[council] = {"avg": None, "max": None, 
                              "min": None, "sum": None}
    return stats


# to test your function with 'sales_data_clean_sample.csv' or another CSV file,
# change the value of this variable
test_file = 'sales_data_clean.csv'
start_date = '01/01/2016'
end_date = '31/12/2017'

# you don't need to modify the code below
if __name__ == '__main__':
    data_cleaned = read_data(test_file)
    pprint(sale_stats_by_council(data_cleaned, start_date, end_date))
