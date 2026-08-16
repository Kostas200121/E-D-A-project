Roller Coaster Exploratory Data Analysis

Project Overview

This project performs exploratory data analysis on a roller coaster dataset using Python, pandas, matplotlib, and seaborn.

The objective is to explore coaster characteristics, identify patterns in the data, visualize distributions and relationships, and examine how features such as speed, height, year introduced, coaster type, and location relate to one another.

This project focuses on data exploration and visualization rather than predictive machine learning.

Dataset

The dataset is stored in:

coaster_db.csv

The original dataset contains:

1,087 rows
56 columns

The analysis focuses on a smaller group of useful variables:

Coaster Name
Location
Status
Opening date
Manufacturer
year_introduced
Type_Main
speed_mph
height_ft

Project Workflow

The script covers a typical exploratory data analysis workflow:

Load the roller coaster dataset

Inspect dataset shape, columns, summary statistics, missing values, and duplicates

Select relevant features

Rename columns for readability

Investigate duplicate coaster records

Analyze coaster introductions by year

Explore the distribution of coaster speeds

Examine the relationship between speed and height

Compare numerical features by coaster type

Calculate correlations between numerical variables

Compare average coaster speeds by location

Visualize the results

Data Inspection

The script includes several optional inspection commands for understanding the dataset:

df.shape
df.head()
df.info()
df.describe()
df.isna().sum()
df.duplicated()

These checks help identify the dataset structure, missing values, numerical ranges, and potential duplicate records.

Duplicate Analysis

Duplicate records are checked using:

df.duplicated(
    subset=['Coaster Name', 'Location', 'Opening date']
)

An example coaster is also queried to inspect duplicate entries manually.

Important Note

The current script uses:

df = df.loc[
    df.duplicated(
        subset=['Coaster Name', 'Location', 'Opening date']
    )
]

This keeps only duplicated rows rather than removing duplicates.

With the current dataset, this reduces the analysis from 1,087 records to 97 duplicated records.

If the intended goal is to remove duplicate records while keeping the main dataset, this can be changed to:

df = df.loc[
    ~df.duplicated(
        subset=['Coaster Name', 'Location', 'Opening date']
    )
].reset_index(drop=True)

Exploratory Visualizations

Coasters Introduced by Year

The project identifies the years with the highest number of coaster introductions and displays the top ten using a bar chart.

df['year_introduced']     .value_counts()     .head(10)     .plot(kind='bar')

This helps visualize periods of higher roller coaster development activity.

Speed Distribution

The distribution of coaster speeds is explored using both a histogram and a kernel density estimate.

df['speed_mph'].plot(kind='hist', bins=20)

and:

df['speed_mph'].plot(kind='kde')

These visualizations show the frequency and overall shape of coaster speed values.

Speed vs Height

A scatter plot is used to examine the relationship between coaster speed and coaster height:

df.plot(
    kind='scatter',
    x='speed_mph',
    y='height_ft'
)

A seaborn version also uses the year introduced as a color dimension:

sns.scatterplot(
    data=df,
    x='speed_mph',
    y='height_ft',
    hue='year_introduced'
)

Pairplot

A pairplot compares:

speed_mph
height_ft
year_introduced

while separating observations by coaster type:

sns.pairplot(
    df,
    vars=['speed_mph', 'height_ft', 'year_introduced'],
    hue='Type_Main'
)

This provides a compact visual overview of several relationships within the dataset.

Correlation Analysis

The project calculates a correlation matrix for:

speed_mph
height_ft
year_introduced

using:

df[
    ['speed_mph', 'height_ft', 'year_introduced']
].dropna().corr()

The correlations are displayed using a seaborn heatmap.

sns.heatmap(
    correlation_matrix,
    annot=True,
    vmin=-1,
    vmax=1
)

This helps identify positive and negative relationships between the numerical variables.

Location Analysis

The project groups coaster records by location and calculates:

mean coaster speed
number of coaster records

Locations are then ranked by average coaster speed and displayed using a horizontal bar chart.

This demonstrates the use of:

groupby()
agg()
query()
sort_values()

for analytical data aggregation.

Requirements

Install the required Python packages with:

pip install pandas matplotlib seaborn scipy

Run the Project

Keep the Python script and dataset in the same project folder:

roller-coaster-eda/
    eda.py
    coaster_db.csv
    README.md

For portability, the dataset can be loaded using:

df = pd.read_csv("coaster_db.csv")

Then run:

python eda.py

Skills Demonstrated

This project demonstrates:

pandas data loading and inspection

Data cleaning

Duplicate detection

Feature selection

Column renaming

Missing value handling

Descriptive statistics

Data aggregation with groupby

Histograms and density plots

Scatter plots

Pairplots

Correlation analysis

Heatmap visualization

Exploratory data analysis

matplotlib and seaborn visualization

Possible Improvements

Future improvements could include:

Correct the duplicate filtering step so duplicated rows are removed rather than exclusively retained

Add clearer missing value analysis

Compare coaster manufacturers

Analyze coaster types by average speed and height

Explore how coaster characteristics changed over time

Add additional summary statistics and grouped analyses

Improve chart labels and formatting

Save charts to an images folder for use in the README

Convert repeated plotting logic into reusable functions

Add a conclusions section containing the main findings from the analysis
