import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    # Aggregate rainfall data to yearly totals
    annual_rainfall = ds['rain'].groupby('time.year').sum(dim='time')
    annual_rainfall_df = annual_rainfall.to_dataframe().reset_index()
    annual_rainfall_df = annual_rainfall_df.groupby('year').mean().reset_index()

    # Prepare the dataset for modeling
    X = annual_rainfall_df[['year']]
    y = annual_rainfall_df['rain']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.29, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions and evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Predict future rainfall
    future_years = pd.DataFrame({'year': range(X['year'].max() + 1, X['year'].max() + 11)})
    future_predictions = model.predict(future_years)

    # Plotting the results
    plt.figure(figsize=(12, 6))
    plt.scatter(X_train['year'], y_train, color='blue', label='Training data')
    plt.scatter(X_test['year'], y_test, color='green', label='Testing data')
    plt.plot(X['year'], model.predict(X), color='red', linewidth=2, label='Fitted line')

    # Plotting future predictions
    plt.plot(future_years['year'], future_predictions, color='orange', linewidth=2, linestyle='--', label='Future predictions')

    plt.title('Rainfall Prediction')
    plt.xlabel('Year')
    plt.ylabel('Annual Rainfall (mm)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Example: Create a summary DataFrame
    summary_df = pd.DataFrame({
        'Year': X['year'].tolist() + future_years['year'].tolist(),
        'Actual Rainfall': y.tolist() + [None]*len(future_years),
        'Predicted Rainfall': model.predict(X).tolist() + future_predictions.tolist()
    })

    print(summary_df)