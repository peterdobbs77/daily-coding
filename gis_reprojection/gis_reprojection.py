import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import earthpy as et

# url = "https://data.milwaukee.gov/api/3/action/datastore_search"
# resourceId = '45c027b5-fa66-4de2-aa7e-d9314292093d'
# limitApi = 10
# # API call to Open MKE Data for liquor license data
# url = url + "?resource_id={}&limit={}".format(resourceId, limitApi)
# r = requests.get(url).json()
# # print(json.dumps(r, indent=4))
# print('Data query success:', r['success'])

# if(not r['success']):
#     exit()

# # If data query is successful, let's play with the data!
# data = r['result']
# df = pd.DataFrame(data['records'])

# df['CITY'] = "Milwaukee, WI"  # add city, state to help geo location
# print(df.head())

# address = df[['HOUSE_NR', 'SDIR', 'STREET', 'STTYPE', 'CITY']].apply(
#     lambda x: ' '.join(map(str, x)), axis=1)
# print(address)

citylimit = gpd.read_file('shape/citylimit/citylimit')

print(citylimit.crs)
