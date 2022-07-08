# Data-Analysis-of-house-property-sales
Data analysis of house/property sales in metropolitan Melbourne from 2016 to 2017

This project is handling a dataset of house/property sales in metropolitan Melbourne during the years 2016 and 2017.

The sales data in this project contains the following columns:

* ID: Row record ID.
* Suburb: The suburb where the property is located.
* Address: The property address.
* Postcode: The property postcode, a 4-digit number.
* CouncilArea: The municipality or council area under which the property falls.
* Regionname: The region of metropolitan Melbourne under which the property falls.
* Price: How much the property sold for. This value is a whole number.
* SaleDate: The date of property sale, in the dd/mm/yyyy format.
* Seller: The real estate agency that sold the property.
* Bedrooms: Number of bedrooms.
* Bathrooms: Number of bathrooms.
* CarSpaces: Number of car spaces.
* Landsize: Size of the land. This value is a whole number.
* Latitude: The latitude geolocation coordinate of the property
* Longitude: The longitude geolocation coordinate of the property

Here is a sample of the real estate sales data:
```
ID,Suburb,Address,Postcode,CouncilArea,Regionname,Price,SaleDate,Seller,Bedrooms,Bathrooms,CarSpaces,Landsize,Latitude,Longitude
1,Coburg,8 Watchtower Rd,3058,Moreland,Northern Metropolitan,675000,4/02/2016,Walshe,3,1,2,142,-37.7382,144.973 
2,Abbotsford,25 Bloomburg St,3067,Yarra,Northern Metropolitan,1035000,4/02/2016,Biggin,2,1,0,156,-37.8079,144.9934
3,Richmond,234 Coppin St,3121,Yarra,Northern Metropolitan,1102000,4/02/2016,Dingle,3,2,0,194,-37.8265,145.0022
4,Jacana,11/1051 Pascoe Vale Rd,3047,Hume,Northern Metropolitan,280000,16/04/2016,Raine,2,1,1,197,-37.6859,144.9164
```

A quick explanation of each files:
- **program.py**
> The file where you will write your code. We have included a little bit of code in program.py to get you started.
- **header.py**
> A file containing some useful functions and constants. We have already imported the relevant functions and constants for you in each question.

## Quest 1: Data Cleaning
You have been provided with CSV files containing data about real estate sales in Melbourne. Unfortunately, the data is 'noisy': some people have made data entry mistakes, or intentionally entered incorrect data. Your first task is to clean up the noisy data for later analysis.

There are a few particular errors in this data:
- Typos have occurred in the Price column, resulting in some non-numeric values.
- People have entered Regionname values that are no longer current, valid region names. The valid regions are listed in a list called **VALID_REGION_NAMES**, which is given to you.
- Some people have formatted the sale date incorrectly, such that it is either not of the form dd/mm/yyyy or contains invalid dates, such as 31/11/2016. If a date does not fall under the year 2016 or the year 2017, it is also considered invalid.
- Some Postcode values are not valid Melbourne postcode values: they need to be 4-digit integers that start with 3.

Write a function **clean_sales_data(data)** which takes one argument, a dictionary of data in the format returned by **read_data**. This data has been read directly from a CSV file, and is noisy. Your function should construct and return a new data dictionary which is identical to the input dictionary, except that invalid data, as described by the rules above, have been replaced with None. In doing so, **your program should aim to not modify the input argument dictionary**, data.

There is also one further type of potential error in the noisy data that needs to be fixed. Valid values in the CouncilArea column must be in the set of Melbourne council areas: Banyule, Brimbank, Darebin, Hume, Knox, Maribyrnong, Melbourne, Moonee Valley, Moreland, Whittlesea and Yarra. This list of valid councils can be found in the list **VALID_COUNCIL_AREAS**, which is given to you.

However, values in the CouncilArea column could be incorrectly spelt or contain extra characters. Examples of such incorrect values are: Morelnd; Yara; nox; aDarebin; Melbun; Honey Valley.

Your program should attempt to replace incorrect values with their correct council area value by using the following set similarity measure, which we use to provide a number representing the similarity between two strings. Suppose we have the following two example strings:

string1 = "Aaa bBb ccC" # The set representation of string1 is {'a', 'b', 'c', ' '}

string2 = "bbb ccc ddd" # The set representation of string2 is {'b', 'c', 'd', ' '}

Notice that for our purposes/definition case does not matter (e.g. 'A' is the same as 'a') and that space is also a character.

The set similarity (Sim) measure for string1 and string2 is given by the formula:

$$Sim(string1,string2)=\frac{|S1\cap S2|}{|S1\cup S2|}$$

Where ∩ is set intersection, ∪ is set union, and |X| is the length of set X

So, for example:

$$Sim(string1,string2)=\frac{|a,b,c,(space)\cap b,c,d,(space)|}{|a,b,c,(space)\cup b,c,d,(space)|}=\frac{|b,c,(space)|}{|a,b,c,d,(space)|}=\frac{3}{5}=0.6$$
 
Now, when your program comes across an incorrect council area value it should compare that incorrect value with all of the correct council area strings using the Sim function, and then replace the incorrect string with the valid council area value that it has the highest Sim measure with.

For example, when the incorrect value is "Melbun", the measure comparisons are:
```
Sim("Banyule", "Melbun") = 0.625
Sim("Brimbank", "Melbun")  = 0.3
Sim("Darebin", "Melbun") = 0.3
Sim("Hume", "Melbun")  = 0.42857142857142855
Sim("Knox", "Melbun") = 0.1111111111111111
Sim("Maribyrnong", "Melbun") = 0.25
Sim("Melbourne", "Melbun")  = 0.75
Sim("Moonee Valley", "Melbun")  = 0.36363636363636365
Sim("Moreland", "Melbun")  = 0.4
Sim("Whittlesea", "Melbun")  = 0.16666666666666666
Sim("Yarra", "Melbun")  = 0.0
```

Since Sim("Melbourne", "Melbun") is the highest of all these values, the incorrect "Melbun" would be replaced by "Melbourne".

In cases where an incorrect string has the same similarity score with two or more correct council area values, since the program can't decide on which one might be correct, it just replaces the incorrect value with None. For example, when the incorrect council area string value is "Meorln", the two highest similarities with correct council area values are:

Sim("Moreland", "Meorln") = Sim("Melbourne", "Meorln") = 0.75

Since the program has no further way of deciding between the two, it just replaces "Meorln" with None.

## Quest 2: Sales Statistics
Write a function called **sale_stats_by_council(data, start_date, end_date)** which takes three arguments: a dictionary of clean data in the format returned by read_data, a start date of the form dd/mm/yyyy, and an end date of the form dd/mm/yyyy (both inclusive). You can assume date inputs are valid.

For each council area, the function calculates the following four statistics within the start_date to end_date range:

- average sale Price, rounded to the closest whole number.
- sum total Price
- minimum instance of Price
- maximum instance of Price

If the start date is greater than the end date the function should return -1. You can use Python date functionality to compare two dates. Googling will help you to find ways that this can be done.

The result is a dictionary with this information, as shown in the examples below. If a council does not have this information present in the data, then the values for that council are set to None.

## Quest 3: Sales by Geolocation
For this question you are to write a function **get_avg_price_by_georegion(data, coordinates, width, height)**. The following three input parameters of this function do the following:
- **coordinates** is a tuple of the form (latitude, longitude), where latitude and longitude are float numbers representing geolocation positions.
- **width** is the width in degrees (float number) of a rectangle whose central point is (latitude, longitude)
- **height** is the height in degrees (float number) of a rectangle whose central point is (latitude, longitude)

So, for example, suppose the geolocation coordinates of the point were (-37.840935, 144.946457), and the rectangle width = 0.2 and the rectangle height = 0.1. In that case we have a rectangle with the following geolocation coordinates that looks like this:
![geolocation_sample](https://groklearning-cdn.com/problems/HLsuZzTDLX8fRRPRBsQ8T9/geolocation_square.png)

Note that:
- for the coordinates (x, y), height changes the x value and width changes the y value.
- for the x coordinate, the further up on the rectangle the higher the x value.
- for the y coordinate, the further to the right of the triangle the higher the y value.

Given the inputs of coordinates, width and height, and the resulting geo rectangle, the **get_avg_price_by_georegion** function should return the average price of all the sold properties whose geolocation coordinates fall within the boundaries (including the edges) of the geo rectangle. Return None if there is no property within the region.

## Quest 4: JSON to Python and Back

JSON is a widely used syntax for storing and exchanging data. A JSON object is written in key/value pairs, and a set of objects is surrounded by curly braces {}. For example, such a JSON data structure would look like:
```
{"key1": "string1", "key2": number1, "key3": number2}
```
Notice that keys are always enclosed in "", but for values, strings are enclosed in "" and numbers are not.

Regarding our Melbourne real estate sales data, an example record would be represented in JSON as:
```
{'Address': '85 Turner St',
 'Bedroom': 2,
 'Car': 1,
 'CouncilArea': 'Yarra',
 'Date': '3/12/2016',
 'Landsize': 202,
 'Latitude': -37.7996,
 'Longitude': 144.9984,
 'Postcode': 3067,
 'Price': 1480000,
 'Regionname': 'Northern Metropolitan',
 'Rooms': 2,
 'Seller': 'Biggin',
 'Suburb': 'Abbotsford'}
``` 
To represent a collection of records, we separate each record by a comma and wrap them around square brackets []. You can read more about JSON here: https://www.w3schools.com/js/js_json_intro.asp

For this question you will write a function **provide_realestate_info(main_data, queried_properties)**, where the input **queried_properties** is a JSON structure. This input structure contains the core address information (Suburb, Address and Postcode) for a set of properties and looks like the following example:
```
[
 {"Suburb": "Rosanna", "Address": "7 Hylton Cr", "Postcode": 3084},
 {"Suburb": "Preston", "Address": "3/152 Tyler St", "Postcode": 3072},
 {"Suburb": "Epping", "Address": "19 Houston St", "Postcode": 3076}
]
```
The function **provide_realestate_info** will return a JSON-style dictionary structure that adds more information to the input structure as follows. For each property in this input set, the **provide_realestate_info** function should search the main dataset for a record of this property. If the record for a property is found, then add the key/value elements for the fields *Price, Bedrooms and Landsize*. If the input property record is not found, then remove it from the set.

Moreover, there could be some JSON input entries that have street names but no number, such as
```
{"Suburb": "Rosanna", "Address": "Hylton Cr", "Postcode": 3084}.
```
In this case, if a **single** match with "Hylton Cr" could be found, then that property information would be returned. However, if the CSV data set had **more than one address** at "Hylton Cr", then no information for that JSON entry would be returned because there is no way to decide which of the properties it is.
