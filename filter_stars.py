import plotly.express as px
import pandas as pd
import matplotlib

info = pd.read_csv('./Nuevo.csv')
stars = pd.DataFrame(info)
stars_years = []
stars_years_gravity = []

stars.info()
stars['Distance']=stars['Distance'].apply(lambda  x: x.replace('$', '').replace(',', '')).astype('float')
stars.info()
#Ha este tambien pasa algo con los datos de str a int :(
for star_data in stars:
    if(star_data[3] <= 100):
        stars_years.append(star_data[3])

for star_data in stars_years:
    if(star_data[6] >= 150 and star_data[6] <= 350 ): 
        stars_years_gravity.append(star_data[3])

print(stars_years_gravity)
filtered_stars = pd.DataFrame(stars_years_gravity)
filtered_stars.to_csv("Filtered_stars.csv")