import pandas as pd
import plotly.express as px

# download data
df = pd.read_csv('estimated_crimes_1979_2020.csv')

# research of the structure and types of data
print(df.info())
print(df.head(10))

# filter data
df = df[df['state_abbr'].notna()].copy()
df = df.loc[(df['year'] >= 2000)].copy()

# rename columns
df = df.rename(columns={'population': 'Population', 'state_name': 'State', 'state_abbr': 'Abbr', 'year': 'Year'})

# change datatype of columns in order to sum necessary numeric columns
df['Population'] = df['Population'].apply(str).copy()
df['Year'] = df['Year'].apply(str).copy()

# sum all kind of crimes to get the total number of crimes
df['Number of crimes'] = (df.sum(axis=1, numeric_only=True).copy()).astype(int)
print(df.head(10))

# change datatype of 'Population' columns to calculate crime rate per 100000 inhabitants
df['Population'] = df['Population'].apply(int).copy()
df['Crime rate per 100k'] = round(df['Number of crimes'] / (df['Population']/100000),2).astype(int)

# create a processed final table
result = df[['Year','Abbr','State','Population','Number of crimes','Crime rate per 100k']].copy()
print(result.head(10))


# aggregate data to get max and min values to set up "range_color"
min_max = result.groupby('State').agg({'Crime rate per 100k': ['min', 'max']})

print(min_max.min())
print(min_max.max())

# create choropleth map to show crime rate in the U.S. since 2000 to 2020
viz = px.choropleth(data_frame=result,
                    locations='Abbr',
                    locationmode='USA-states',
                    color = 'Crime rate per 100k',
                    color_continuous_scale='YlOrRd',
                    title = "CRIME RATE IN THE USA SINCE 2000",
                    animation_frame = 'Year',
                    hover_data={'Year': False, 'State':True,'Number of crimes': True, 'Abbr': False, 'Population':True, 'Crime rate per 100k':False},
                    range_color=[2490,16093],
                    projection='albers usa')

viz.add_scattergeo(
    locations=result['Abbr'],
    locationmode="USA-states",
    hoverinfo = 'none',
    marker_size = 50,
    text=result['Abbr'],
    mode='text',
)
viz.update_layout(title_text='CRIME RATE IN THE USA SINCE 2000', title_x=0.5)
viz.show()