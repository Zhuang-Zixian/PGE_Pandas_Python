import pandas as pd

class VisitorAnalyticsUtils:
    def loadDataFile (self):
        # making a dataframe from csv file declare header and index columns nan values for cleaning data
        df = pd.read_csv("Int_Monthly_Visitor.csv", header = 0, index_col = 0, na_values=" na ", thousands=",")
        df = df.fillna(value= 0)
        return df


    def parseData (self, df, startYear, endYear, countries):
        startYear = str(startYear) + ' Jan'
        endYear = str(endYear) + ' Dec'
        df = df.assign(year_month = df.index.str.strip())
        df.index = df['year_month']
        year_month_df = df['year_month'].str.split(" ", n = 1, expand = True)
        df = df.assign(year = year_month_df[0])
        df = df.drop([ 'year_month' ],axis=1)
        region_df = df[countries]
        region_df = region_df.assign(year = year_month_df[0])
        region_df = region_df.astype('int64')
        region_time_df = region_df.loc[startYear:endYear]
        return region_time_df


    def getTop3Countries (self, regionTimeDf):
        #code goes here
        region_only_df = regionTimeDf.drop([ 'year' ],axis=1)
        sorted_by_visitor_no = regionTimeDf.sum(axis = 0, skipna = True)
        top_3_countries = sorted_by_visitor_no.sort_values(ascending=False)
        top_3_countries = top_3_countries.head(3)
        
        return top_3_countries

