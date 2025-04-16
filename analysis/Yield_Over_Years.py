import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": ["2014/2015", "2015/2016", "2016/2017", "2017/2018", "2018/2019", "2019/2020", "2020/2021", "2021/2022", "2022/2023"],
    "Area (1000 Ha)": [44110, 43499, 43994, 43774, 44156, 43662, 45769, 46279, 47832],
    "Milled Production (1000 Tons)": [105482, 104408, 109698, 112758, 116484, 118870, 124368, 129471, 135755],
    "Rough Production (1000 Tons)": [158239, 156628, 164563, 169154, 174743, 178323, 186571, 194226, 203653],
    "Yield (T/Ha)": [3.6, 3.6, 3.7, 3.9, 4.0, 4.1, 4.1, 4.2, 4.3]
}

df = pd.DataFrame(data)

df.columns = df.columns.str.strip()

# Extract the starting year from the "Year" column and convert to integer
df['Year'] = df['Year'].apply(lambda x: int(x.split('/')[0]))

# Check the column names
print(df.columns)

# Plotting Yield over Years
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Yield (T/Ha)'], marker='o', linestyle='-', color='b')
plt.title('Yield over Years')
plt.xlabel('Year')
plt.ylabel('Yield (T/Ha)')
plt.xticks(df['Year'], rotation=45)  # Ensures all years are shown on x-axis
plt.grid(True)
plt.show()
