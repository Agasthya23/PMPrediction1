
#importing libraries
import pandas as pd
import glob


#extracting table from downloaded HTML pages
def met_data(month, year):
    file = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb')
    data=pd.read_html(file,attrs={'class': 'medias mensuales numspan'})
    table=data[0]
    return table

#extracting PM10 values from local folder that was downloaded
#PM 10 values source Central control room for air quality mgmt website
    
def pm():
    series_list=[]
    #retrieving csv file data containing PM10 values
    filenames = glob.glob(r'C:\Users\HP\Desktop\Project2\AQI\Pmdata\*.csv')
    for f in filenames:
            data=pd.read_csv(f,encoding='utf-8')
            #selecting only PM10 column
            a=data.PM10
            series_list.append(a)
    return series_list

if __name__ == "__main__":
    features=[]
    for year in range(2016, 2021):
        for month in range(1, 13):
            temp = met_data(month, year)
            #dropping features that are features
            temp=temp.drop(['Day','SLP','VG','RA','SN','TS','FG'],axis=1)
            #dropping rows that are irrelevant
            temp=temp.iloc[:-2]
            features.append(temp)
    
    #combining list of dataframes to one single dataframe 
    df=pd.concat(features,axis=0,ignore_index=True)
    
    #calling dependent feature
    dependent= pm()
    #combining list of series to one series
    dependent=pd.concat(dependent,axis=0,ignore_index=True)
    
    #merging the series to the dataframe
    df=df.merge(dependent,left_index=True,right_index=True)
    
    #exporting data to csv file
    df.to_csv('New_data.csv')
    
    
    

            

             