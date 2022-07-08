from header import read_data


def get_avg_price_by_georegion(data, coordinates, width, height):
    """
    This function is to calculate the average sale prices of properties whose
    geolocation fall within the geo rectangle.
    
    Args:
        data (dict): a dictionary of clean data returned by read_data.
        coordinates (tuple): a tuple of the form (latitude, longitude), where
          latitude and longitude are float representing geolocation positions.
        width (float): width of a rectangle central at (latitude, longitude).
        height (float): height of a rectangle central at (latitude, longitude).

    Returns:
        average_price (float): the average sale prices of properties whose 
          geolocation fall within the geo rectangle; or
        None (NoneType): if there is no property within the region.
    """
    latitude_range = [coordinates[0] - height / 2, coordinates[0] + height / 2]
    longitude_range = [coordinates[1] - width / 2, coordinates[1] + width / 2]
    
    prices = []
    for info in data.values():
        latitude = float(info["Latitude"])
        longitude = float(info["Longitude"])
        if latitude_range[0] <= latitude <= latitude_range[1] and \
           longitude_range[0] <= longitude <= longitude_range[1]:
            prices.append(int(info["Price"]))
    
    # if the list of prices is not empty, calculate the result.
    if prices:
        average_price = round(sum(prices) / len(prices))
        return average_price
    return None


# to test your function with another CSV file,
# change the value of this variable
test_file = 'sales_data_clean.csv'
coordinates = (-37.841935, 144.816457)
width = 0.2
height = 0.1

# you don't need to modify the code below
if __name__ == '__main__':
    data_cleaned = read_data(test_file)
    print(get_avg_price_by_georegion(data_cleaned, coordinates, width, height))
