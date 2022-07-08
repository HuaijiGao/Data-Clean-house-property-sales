# Data-Clean-house-property-sales
Data cleaning of house/property sales in metropolitan Melbourne from 2016 to 2017

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
- People have entered Regionname values that are no longer current, valid region names. The valid regions are listed in a list called VALID_REGION_NAMES, which is given to you.
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
