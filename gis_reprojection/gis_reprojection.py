#import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import json
from geopy.geocoders import Nominatim

print('start program')

citylimit = gpd.read_file('gis_reprojection/shape/citylimit/citylimit.shp')
print(citylimit.crs)

fig, ax = plt.subplots(figsize=(12, 8))
citylimit.plot(ax=ax)  # (cmap='Greys', ax=ax, alpha=0.5)
ax.set_title('Milwaukee, WI')
plt.show()
