import pandas as pd
import time
import numpy as np

# Import the pre-prepared webpage index specific to this scrape
webpages_index = pd.read_csv('webpages_index.csv')
#print(webpages_index)

# Initiate temp dataframe file to collect scrapped tables
names_temp = pd.DataFrame()

# Initiate dataframe file to append scrapped tables to
names = pd.DataFrame()

# Initiate list file to append page numbers to
repeat = []

# Initiate list file to append url list to
urls = []
urls2 = urls[0:20]

# Sample scaping format of pd.read_html        
# dfs_temp = pd.read_html('https://adoption.com/baby-names/browse/A?page=1')[0]

# Loop to create url list from the information in the webpages_index file
for key, value in webpages_index.iterrows():
    letters = webpages_index.loc[key,'letter'] 
    for i in letters:
        repeat = webpages_index.loc[key,'pages']
        for j in range(1,repeat+1):
            urls.append ('https://adoption.com/baby-names/browse/'+i+'?page='+str(j))

# Loop to scrape the names data from the website and append it in the initiated dataframe
print('Estimated time to complete: approximately', 
      round((len(urls)*10/60),1) ,
      'minutes','or', 
      round((len(urls)*10/60)/60,1) ,'hours')
for i in urls2:
    names_temp = pd.read_html(i, header=0)[0]
    # Time delay of 3 to 15 seconds is given for the webpage to load
    #time.sleep(2)
    time.sleep(np.random.randint(3,15))
    names = names.append(names_temp, ignore_index=True)
    print(i,'done')

# Export the collected data to a excel file in disc
names.to_excel('C:/Users/Mathu/Desktop/GNS Automation/Names_Master_Full.xlsx', index=False)
