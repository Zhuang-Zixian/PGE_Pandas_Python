import pandas as pd
from utils import VisitorAnalyticsUtils

countriesEuro = [' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',
       ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
       ' Scandinavia ', ' CIS & Eastern Europe ']
countriesAsia = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ',
       ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ', ' Hong Kong ',
       ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ', ' Pakistan ',
       ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']
countriesOthers = [' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']
countries = countriesOthers

start_year = 1978
end_year = start_year + 9

#Get user input for year period
region_Choice = input("1: Asia, 2: Europe, 3: Others):")

if(region_Choice.isnumeric()):
    region = int(region_Choice)
    if region == 1:
        countries = countriesAsia
    elif region == 2:
        countries = countriesEuro
    elif region == 3:
        countries = countriesOthers
    else:
        print("Invalid input, exit program")
        exit(0)
        
else:
    print("Invalid input, exit program.")
    exit(0)

period = input("Enter year period (1: 1978-1987, 2: 1988-1997, 3: 1998-2007, 4: 2008-2017):")

if(period.isnumeric()):
    year_choice = int(period)
    
    if year_choice == 1:
        start_year = 1978
    elif year_choice == 2:
        start_year = 1988
    elif year_choice == 3:
        start_year = 1998
    elif year_choice == 4:
        start_year = 2008
    else:
        print("Invalid input")
        exit(0)

    #Setting endYear to 9 years more than startYear
    end_year = start_year + 9

else:
    print("Invalid input, exit program.")
    exit(0)

utils = VisitorAnalyticsUtils()


raw_dataframe = utils.loadDataFile()
print("*** first 5 rows of data loaded ***")
#print(raw_dataframe.head())

region_time_dataframe = utils.parseData(raw_dataframe, start_year, end_year, countries)
region_time_dataframe2 = region_time_dataframe.drop([ "year" ],axis=1)
print(region_time_dataframe2.head())
print("")

print("*** Parsed Data (Regions) ***")
print(region_time_dataframe.info())
print("")

print("*** Parsed Data (Years) ***")
print(region_time_dataframe["year"].describe())
print("")

print("*** Top 3 countries ***")
print(utils.getTop3Countries(region_time_dataframe))
print("")


