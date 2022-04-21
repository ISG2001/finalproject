import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------
# PART 1 - Exploratory Data Analysis
# ----------------------------------------------------------------------------------------------------------------------

# Load .csv file as a dataframe with pandas
path_file = '/Users/ikersanudo/PycharmProjects/GroupProje/smstocks2012-22.csv'
data = pd.read_csv(path_file)
# Data source: https://finance.yahoo.com/

# Check data type - It is a pandas dataframe
print("\nData type:")
print(type(data))

# Check headings and some rows
print("\nOverlook of dataframe:")
pd.set_option("display.max_columns", None)
print(data.head(10))
print(data.tail(10))

# Check each data type of columns and missing values
print("\nData info:")
data.info()
# There is 8,398 rows (data points), and 8 columns
# There are no missing values

# Summary of statistics of numeric variables
print(data.describe())
# We do not obtain interesting information for the analysis
# We can try to find statistics for each company
# Also, we will not use the adj close, high or low columns in our analysis

# Selecting the needed columns
data = data[['Symbol', 'Date', 'Close', 'Volume']]
# Closing price is most relevant

# Check new dataframe and changed data type
print("\nData info (updated):")
data.info()

# Look per company (choosing symbol)
print("\nNumber of days in trading per company:")
print(data.Symbol.value_counts())
# FB has been there for 2488 days, TWTR for 2118 days, ETSY for 1758 days, SNAP for 1285 days and PINS for 749

# We are creating a new data set for each company, only with its data filtered
data_fb = data[data["Symbol"] == "FB"]
data_twtr = data[data["Symbol"] == "TWTR"]
data_etsy = data[data["Symbol"] == "ETSY"]
data_snap = data[data["Symbol"] == "SNAP"]
data_pins = data[data["Symbol"] == "PINS"]

# Statistical summaries for each company
print("\nStatistics - FB:")
print(data_fb.describe())
# Mean closing price of 147, min of 17, max of 382
print("\nStatistics - TWTR:")
print(data_twtr.describe())
# Mean closing price of 35, min of 14, max of 77
print("\nStatistics - ETSY:")
print(data_etsy.describe())
# Mean closing price of 68, min of 6, max of 296
print("\nStatistics - SNAP:")
print(data_snap.describe())
# Mean closing price of 26, min of 4, max of 83
print("\nStatistics - PINS:")
print(data_pins.describe())
# Mean closing price of 40, min of 10, max of 89

# Highest closing price is unsurpisingly Facebook
# The second highest both in mean and max is surprisingly Etsy
# The lowest out of the 5 is Snapchat

## Make a table with this data? For the slides

# ----------------------------------------------------------------------------------------------------------------------
# PART 2 - Visualizing the Data - Basic
# ----------------------------------------------------------------------------------------------------------------------

# Histograms

# Close Price Histogram for Facebook
close_fb = data_fb["Close"]
plt.hist(close_fb, color="blue", ec="black", lw=1)
plt.title('Close Price for Facebook')
plt.xlabel('Price in US$')
plt.ylabel('Frequency (number of days')
plt.show()

# Close Price Histogram for Twitter
close_twtr = data_twtr["Close"]
plt.hist(close_twtr, color="skyblue", ec="black", lw=1)
plt.title('Close Price for Twitter')
plt.xlabel('Price in US$')
plt.ylabel('Frequency (number of days')
plt.show()

#Close Price Histogram for Etsy
close_etsy = data_etsy["Close"]
plt.hist(close_etsy, color="orange", ec="black", lw=1)
plt.title('Close Price for Etsy')
plt.xlabel('Price in US$')
plt.ylabel('Frequency (number of days')
plt.show()

# Close Price Histogram for Snapchat
close_snap = data_snap["Close"]
plt.hist(close_snap, color="yellow", ec="black", lw=1)
plt.title('Close Price for Snapchat')
plt.xlabel('Price in US$')
plt.ylabel('Frequency (number of days')
plt.show()

# Close Price Histogram for Pinterest
close_pins = data_pins["Close"]
plt.hist(close_pins, color="red",  ec="black", lw=1)
plt.title('Close Price for Pinterest')
plt.xlabel('Price in US$')
plt.ylabel('Frequency (number of days')
plt.show()

# Include short analysis of the distribution for each
# However, we do not know the evolution because it only shows the frequency
# and not a time series. We will find this later on.

# Barchart of mean closing price per company

company = ("FB", "TWTR", "ETSY", "SNAP", "PINS")
price = (close_fb.mean(), close_twtr.mean(), close_etsy.mean(), close_snap.mean(), close_pins.mean())
y_pos = np.arange(len(company))
colors = ['blue', 'skyblue', 'orange', 'yellow', 'red']
plt.bar(y_pos, price, color=colors, align='center')
plt.xticks(y_pos, company)
plt.title('Mean closing price for top 5 companies ')
plt.xlabel('Price in USD$')
plt.ylabel('Company Symbol')
plt.show()

# Boxplots

# Boxplot of trade volume for Facebook
volume_fb = data_fb["Volume"]
plt.boxplot(volume_fb, sym='gx', widths=0.75, notch=True)
plt.title('Boxplot of Facebooks trade volume')
plt.show()
# There are way too many outliers in the trade volume for the boxplot to be interpretable
# Most days have very low trade volume, and there are a small number that have high or extremely
# high trade volume. Is there a correlation between volume and closing price

# Scatterplots

volume_twtr = data_twtr["Volume"]
volume_etsy = data_etsy["Volume"]
volume_snap = data_snap["Volume"]
volume_pins = data_pins["Volume"]

# Correlation between closing price and volume for Facebook
plt.scatter(close_fb, volume_fb, marker='o', c='b')
plt.title('Correlation between closing price and volume for Facebook')
plt.xlabel('Closing price in US$')
plt.ylabel('Trade volume')
plt.show()

# Correlation between closing price and volume for Twitter
plt.scatter(close_twtr, volume_twtr, marker='o', c='m')
plt.title('Correlation between closing price and volume for Twitter')
plt.xlabel('Closing price in US$')
plt.ylabel('Trade volume')
plt.show()

# Correlation between closing price and volume for Etsy
plt.scatter(close_etsy, volume_etsy, marker='o', c='g')
plt.title('Correlation between closing price and volume for Etsy')
plt.xlabel('Closing price in US$')
plt.ylabel('Trade volume')
plt.show()

# Correlation between closing price and volume for Snapchat
plt.scatter(close_snap, volume_snap, marker='o', c='y')
plt.title('Correlation between closing price and volume for Snapchat')
plt.xlabel('Closing price in US$')
plt.ylabel('Trade volume')
plt.show()

# Correlation between closing price and volume for Pinterest
plt.scatter(close_pins, volume_pins, marker='o', c='r')
plt.title('Correlation between closing price and volume for Pinterest')
plt.xlabel('Closing price in US$')
plt.ylabel('Trade volume')
plt.show()

# From an initial glance, we can learn that there are no correlation between
# closing price and volume trade for any of the companies

# ----------------------------------------------------------------------------------------------------------------------
# PART 3 - Visualizing the Data 2
# ----------------------------------------------------------------------------------------------------------------------

# Comparing the four companies along time

print(len(data_fb))
print(len(data_twtr))
print(len(data_snap))
print(len(data_etsy))
print(len(data_pins))

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(data_fb, data_twtr, data_snap, data_etsy, data_pins)
plt.show()

#Given that the length of the dataframes are not the same, as not all companies were introduced into the stock market
#at the same time, if we try to perform a plot, all of them will start by default on index 0, and therefore we need
#to create 'blank' rows so that each company starts at their corresponding actual year.
#The main reason why we didn't modify the x label to be temporal, is because the stock market doesn't function during
#the weekends are there were therefore important gaps that had to be taken into account

#Twtr length modification for basic graph
lengthtwtr = len(data_fb) - len(data_twtr)
print(lengthtwtr)
df_twtr2 = pd.DataFrame([0], columns=['Close'])
df_twtr2 = df_twtr2.reindex(df_twtr2.index.repeat(lengthtwtr)).reset_index(drop=True)
print(len(df_twtr2))
df_twtr3 = pd.concat([data_twtr, df_twtr2]).reset_index(drop=True)
data_twtr1 = df_twtr3
#Put the last rows, those which we converted into 0 values into the first rows, so that they appear as the first years
data_twtr1 = data_twtr1.apply(np.roll, shift=lengthtwtr)
print(data_twtr1.head(3))
print(data_twtr1.tail(3))
close_twtr1 = data_twtr1["Close"]

#Etsy length modification for basic graph
lengthetsy = len(data_fb) - len(data_etsy)
print(lengthetsy)
df_etsy2 = pd.DataFrame([0], columns=['Close'])
df_etsy2 = df_etsy2.reindex(df_etsy2.index.repeat(lengthetsy)).reset_index(drop=True)
print(len(df_etsy2))
df_etsy3 = pd.concat([data_etsy, df_etsy2]).reset_index(drop=True)
data_etsy1 = df_etsy3
#Put the last rows, those which we converted into 0 values into the first rows, so that they appear as the first years
data_etsy1 = data_etsy1.apply(np.roll, shift=lengthetsy)
close_etsy1 = data_etsy1["Close"]

#Snap length modification for basic graph
lengthsnap = len(data_fb) - len(data_snap)
print(lengthsnap)
df_snap2 = pd.DataFrame([0], columns=['Close'])
df_snap2 = df_snap2.reindex(df_snap2.index.repeat(lengthsnap)).reset_index(drop=True)
print(len(df_snap2))
df_snap3 = pd.concat([data_snap, df_snap2]).reset_index(drop=True)
data_snap1 = df_snap3
#Put the last rows, those which we converted into 0 values into the first rows, so that they appear as the first years
data_snap1 = data_snap1.apply(np.roll, shift=lengthsnap)
close_snap1 = data_snap1["Close"]

#Pins length modification for basic graph
lengthpins = len(data_fb) - len(data_pins)
print(lengthpins)
df_pins2 = pd.DataFrame([0], columns=['Close'])
df_pins2 = df_pins2.reindex(df_pins2.index.repeat(lengthpins)).reset_index(drop=True)
print(len(df_pins2))
df_pins3 = pd.concat([data_pins, df_pins2]).reset_index(drop=True)
data_pins1 = df_pins3
#Put the last rows, those which we converted into 0 values into the first rows, so that they appear as the first years
data_pins1 = data_pins1.apply(np.roll, shift=lengthpins)
close_pins1 = data_pins1["Close"]

#Plot the close prices for the modified datasets
plt.plot(range(len(data_fb)), close_fb)
plt.plot(range(len(data_twtr1)), close_twtr1)
plt.plot(range(len(data_snap1)), close_snap1)
plt.plot(range(len(data_etsy1)), close_etsy1)
plt.plot(range(len(data_pins1)), close_pins1)
plt.title('Evolution of closing prices of the 5 companies')
plt.xlabel('Days passed since 2012-05-08')
plt.ylabel('Price in USD$')
plt.show()

plt.plot(range(len(data_fb)), close_fb)
plt.plot(range(len(data_twtr1)), close_twtr1)
plt.plot(range(len(data_snap1)), close_snap1)
plt.plot(range(len(data_etsy1)), close_etsy1)
plt.plot(range(len(data_pins1)), close_pins1)






