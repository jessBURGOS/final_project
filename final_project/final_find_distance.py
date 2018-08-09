
import pandas as pd 
import geocoder
import time
from geopy.geocoders import Nominatim
from pyproj import Geod
from itertools import chain

d = pd.read_csv("cleaned_data.csv")


wgs84_geod = Geod(ellps='WGS84') #Distance will be measured on this ellipsoid - more accurate than a spherical method

#Get distance between pairs of lat-lon points
def Distance(lat1,lon1,lat2,lon2):
  az12,az21,dist = wgs84_geod.inv(lon1,lat1,lon2,lat2) #Yes, this order is correct
  return dist

df = d[:500]

d_combinded = []
for x in zip(df['lat'],df['lng']):
        for y in zip(df['lat'],df['lng']):
            d_combinded.append((x,y))
            print (x,y)

o = []
for a in d_combinded:
    print(list(chain.from_iterable(a)))
    o.append(tuple(list(chain.from_iterable(a))))
    
new =[]
for i in o:
        new.append(Distance(*i))
        print(Distance(*i))

#This number should change based on len of columns
new_list = [new[i:i+500] for i in range(0, len(new), 500)]



columns = list(df['property_id'])


# d_2 are column head
#new_list is the data 
df_2=pd.DataFrame(new_list,columns=columns)


new_df =pd.concat([df, df_2], axis=1)

new_df.to_csv('cleaned_data_w_distance_sample.csv', encoding='utf-8', index=False)

