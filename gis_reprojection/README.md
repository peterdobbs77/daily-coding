# gis_reprojection

I missed the first challenge from Daily Coding Problem, since I forgot to verify my email :sob:. So I decided to try out something I have been meaning to explore since I worked on a GIS project a few semesters ago...

While working on a side project to display open data on a GIS map of Milwaukee - [github.com/peterdobbs77/pop_health_mke/blob/master/try_graph_liq.py](link to Python file in GitHub project), I found that there are some odd differences between the way that various data sources are geospatially encoded. For example, here's one of my attempts to plot the location of registered liquor licenses around Milwaukee:

![Example of weird geospatial encodings](images/1574635489.651701.png)

*Apparently there are some liquor stores in Lake Michigan...*

I didn't understand why the geolocations I was retrieving from Nominatim wouldn't overlay onto the shape file I got from the Milwaukee Open Data project. This frustrated me so I left it alone for a while. After a few weeks away from my frustration I stumbled upon [www.earthdatascience.org/workshops/gis-open-source-python/reproject-vector-data-in-python/](this)! It turns out that there are different Coordinate Reference Systems (CRS) for organizing spatial data sets.

So let's get this started.