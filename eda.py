import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import gaussian_kde
plt.style.use('ggplot')
# pd.set_option('max_columns', 200)

df = pd.read_csv('project eda\coaster_db.csv')

#PRINTS
#
#print(df.shape)
#print(df.head(20))
#print(df.info())
#print(df.describe())
#print(df.head())
#print(df.isna().sum())
#print(df.duplicated())

#Check for diplicates
#print(df.loc[df.duplicated(subset=['Coaster Name'])])

#print(df.columns)

#Checking an example duplicate
#print(df.query("`Coaster Name` == 'Crystal Beach Cyclone'"))

#print(df['year_introduced'].value_counts())
#


df = df[['coaster_name', #'Length', 'Speed', 
          'Location', 'Status', 
          'Opening date',#'Type', 
          'Manufacturer',
          #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 'Opened', 'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
      'year_introduced',
      #'latitude', 'longitude', 
      'Type_Main',
       #'opening_date_clean', 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph',
        # 'height_value', 'height_unit', 
        'height_ft',
       #'Inversions_clean', 'Gforce_clean'
       ]].copy()


df = df.rename(columns={'coaster_name': 'Coaster Name'})

df = df.loc[df.duplicated(subset=['Coaster Name', 'Location', 'Opening date'])].reset_index(drop=True).copy()

df.shape

df['year_introduced'].value_counts()\
   .head(10)\
   .plot(kind='bar',
         title='Top 10 Years with the Most Coasters Introduced',
         xlabel='Year Introduced',
         ylabel='Number of Coasters Introduced')

df['speed_mph'].plot(kind='hist', \
                     bins=20,\
                    title='Distribution of Coaster Speeds (MPH)',\
                    xlabel='Speed (MPH)',\
                     ylabel='Frequency')

df['speed_mph'].plot(kind='kde', \
                     title='Distribution of Coaster Speeds (MPH)',\
                    xlabel='Speed (MPH)',\
                     ylabel='Frequency')


df.plot(kind='scatter', x='speed_mph', y='height_ft', \
        title='Scatter Plot of Coaster Speeds (MPH) vs Height (ft)')

ax = sns.scatterplot(data=df, x='speed_mph', y='height_ft' ,hue='year_introduced')
ax.set_title('Scatter Plot of Coaster Speeds (MPH) vs Height (ft) by Year Introduced')

sns.pairplot(df, vars=['speed_mph', 'height_ft', 'year_introduced'], hue='Type_Main')

bro = df[['speed_mph', 'height_ft', 'year_introduced']].dropna().corr()

sns.heatmap(bro, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

brox3 = (df.query('Location != "Other"')\
          .groupby('Location')['speed_mph']\
          .agg(['mean', 'count'])\
          .query('count >= 0')\
          .sort_values('mean')['mean'] 
)

print(brox3)

brox3.plot(kind='barh', figsize=(12, 5),title='Average Coaster Speed (MPH) by Location ')
 
plt.show()