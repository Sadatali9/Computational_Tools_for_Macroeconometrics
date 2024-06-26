import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from numpy.linalg import solve

# Load the dataset
df = pd.read_csv("../REPORT/current.csv")

# Clean the DataFrame by removing the row with transformation codes
df_cleaned = df.drop(index=0)
df_cleaned.reset_index(drop=True, inplace=True)

# Extract transformation codes
transformation_codes = df.iloc[0, 1:].to_frame().reset_index()
transformation_codes.columns = ['Series', 'Transformation_Code']

# Function to apply transformations based on the transformation code
def apply_transformation(series, code):
    if code == 1:
        # No transformation
        return series
    elif code == 2:
        # First difference
        return series.diff()
    elif code == 3:
        # Second difference
        return series.diff().diff()
    elif code == 4:
        # Log
        return np.log(series)
    elif code == 5:
        # First difference of log
        return np.log(series).diff()
    elif code == 6:
        # Second difference of log
        return np.log(series).diff().diff()
    elif code == 7:
        # Delta (x_t/x_{t-1} - 1)
        return series.pct_change()
    else:
        raise ValueError("Invalid transformation code")

# Applying the transformations to each column in df_cleaned based on transformation_codes
for series_name, code in transformation_codes.values:
    df_cleaned[series_name] = apply_transformation(df_cleaned[series_name].astype(float), code)

# Plotting the transformed series
series_to_plot = ['INDPRO', 'CPIAUCSL', 'TB3MS']
series_names = ['Industrial Production', 'Inflation (CPI)', 'Federal Funds Rate']
fig, axs = plt.subplots(len(series_to_plot), 1, figsize=(10, 15))
for ax, series_name, plot_title in zip(axs, series_to_plot, series_names):
    if series_name in df_cleaned.columns:
        dates = pd.to_datetime(df_cleaned['sasdate'], format='%m/%d/%Y')
        ax.plot(dates, df_cleaned[series_name], label=plot_title)
        ax.xaxis.set_major_locator(mdates.YearLocator(base=5))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        ax.set_title(plot_title)
        ax.set_xlabel('Year')
        ax.set_ylabel('Transformed Value')
        ax.legend(loc='upper left')
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    else:
        ax.set_visible(False)
plt.tight_layout()
plt.show()

# Prepare the data for ARX model
Y = df_cleaned['INDPRO'].dropna()
X = df_cleaned[['CPIAUCSL', 'FEDFUNDS']].dropna()

# Set the number of lags for Y and X
h = 1 # One-step ahead
p = 4
r = 4

# Prepare the target variable, lagged variables, and exogenous variables
Y_target = Y.shift(-h).dropna()
Y_lagged = pd.concat([Y.shift(i) for i in range(p+1)], axis=1).dropna()
X_lagged = pd.concat([X.shift(i) for i in range(r+1)], axis=1).dropna()