

#https://en.tutiempo.net/ to get the data

import os
import time
import requests #help us to download that page in the the form of html
import sys #


def retrieve_html():
    for year in range(2016,2021):
        for month in range(1,13):
            if(month)<10:
                #to access data from January to september i.e. 01 -09
                url='http://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
            else:
                #to access data from october i.e. 10
                url='http://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
                
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')

            
            if not os.path.exists("C:/Users/HP/Desktop/Project2/AQI/Data/Html_Data/{}".format(year)):
                #creating year folder
                os.makedirs("C:/Users/HP/Desktop/Project2/AQI/Data/Html_Data/{}".format(year)) 
            #creating month.html file 
            with open("C:/Users/HP/Desktop/Project2/AQI/Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
    
    
    sys.stdout.flush()
    


if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Total Time taken to execute {}".format(stop_time-start_time))
    
    
            
    
        

