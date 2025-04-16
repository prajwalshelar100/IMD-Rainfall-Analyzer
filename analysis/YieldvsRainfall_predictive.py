import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    # Agricultural data
    agri_data = {
        "Year": ["2014/2015", "2015/2016", "2016/2017", "2017/2018", "2018/2019", "2019/2020", "2020/2021", "2021/2022", "2022/2023"],
        "Area (1000 Ha)": [44110, 43499, 43994, 43774, 44156, 43662, 45769, 46279, 47832],
        "Milled Production (1000 Tons)": [105482, 104408, 109698, 112758, 116484, 118870, 124368, 129471, 135755],
        "Rough Production (1000 Tons)": [158239, 156628, 164563, 169154, 174743, 178323, 186571, 194226, 203653],
        "Yield (T/Ha)": [3.6, 3.6, 3.7, 3.9, 4.0, 4.1, 4.1, 4.2, 4.3]
    }

    # Create DataFrame for agricultural data
    agri_df = pd.DataFrame(agri_data)

    # Strip any leading/trailing spaces from column names (if any)
    agri_df.columns = agri_df.columns.str.strip()

    # Extract the starting year from the "Year" column and convert to integer
    agri_df['Year'] = agri_df['Year'].apply(lambda x: int(x.split('/')[0]))

    # Aggregate rainfall data to yearly totals
    annual_rainfall = ds['rain'].groupby('time.year').sum(dim='time')
    annual_rainfall_df = annual_rainfall.to_dataframe().reset_index()
    annual_rainfall_df = annual_rainfall_df.groupby('year').mean().reset_index()

    # Merge with agricultural data
    merged_df = pd.merge(agri_df, annual_rainfall_df, left_on='Year', right_on='year', how='left')
    merged_df.drop(columns=['year'], inplace=True)

    # Prepare the dataset for modeling
    X = merged_df[['rain']]
    y = merged_df['Yield (T/Ha)']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.29, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions and evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Plot actual vs predicted yield
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual Yield')
    plt.plot(X_test, y_pred, color='red', linestyle='-', marker='o', label='Predicted Yield')
    plt.title('Actual vs Predicted Yield')
    plt.xlabel('Annual Rainfall')
    plt.ylabel('Yield (T/Ha)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
