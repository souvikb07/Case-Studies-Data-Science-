The analysis involves integrating multi-DataFrame. 
This is a rich dataset that will allow to fully leverage pandas data manipulation skills.

I'll be using The Guardian's Olympic medal dataset.

The first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.

The second task here is to prepare a DataFrame ioc_codes from a comma-separated values (CSV) file.

Build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.
The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).
Once the dictionary of DataFrames is built up, combine the DataFrames using pd.concat().

Construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic 
edition on the Index and with 138 country NOC codes as columns. If you want a refresher on  pivot tables, it may be useful to refer back to the relevant exercises in 
Manipulating DataFrames with pandas.

Extract a Series with the total number of medals awarded in each Olympic edition.The DataFrame medal_counts can be divided row-wise by 
the total number of medals awarded each edition; the method .divide() performs the broadcast as you require.
This gives you a normalized indication of each country's performance in each edition.

Computing percentage change in fraction of medals won.

Prepare a DataFrame hosts by left joining editions and ioc_codes. Once created, you will subset the Edition and NOC columns and set Edition 
as the Index. There are some missing NOC values; you will set those explicitly. Reset the Index & print the final DataFrame.

Merge the two DataFrames and tidy the result. The end result is a DataFrame summarizing the fractional change in the expanding mean of the 
percentage of medals won for the host country in each Olympic edition.

Plotting influence of host country
