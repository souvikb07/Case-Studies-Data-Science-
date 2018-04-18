#Visualizing USA Medal Counts by Edition: Line Plot

#import pandas
import pandas as pd

#import matplotlit
import matplotlib.pyplot as plt

#file path
file_path_editions = 'Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.csv'

#create medals dataframe
medals = pd.read_csv(file_path_editions)

# Create the DataFrame: usa
usa = medals[medals.NOC=='USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()


#Visualizing USA Medal Counts by Edition: Area Plot

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()


#Visualizing USA Medal Counts by Edition: Area Plot with Ordered Medals

# Redefine 'Medal' as an ordered categorical
medals.Medal = pd.Categorical(values = medals.Medal, categories=['Bronze', 'Silver', 'Gold'], ordered=True)

# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()
