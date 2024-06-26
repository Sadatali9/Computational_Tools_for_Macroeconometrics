# Project: Computational Tools for Macroeconometrics

## Table of Contents
1. [Introduction](#introduction)
2. [Data Description](#data-description)
3. [Objectives](#objectives)
4. [Installation and Setup](#installation-and-setup)
5. [Running the Code](#running-the-code)
6. [Output and Results](#output-and-results)
7. [Troubleshooting and Known Issues](#troubleshooting-and-known-issues)

## Introduction
This project introduces students to practical and theoretical aspects of macroeconometrics, focusing on forecasting using the FRED-MD dataset. The FRED-MD dataset is a comprehensive monthly database for macroeconomic research compiled by the Federal Reserve Bank of St. Louis, featuring a wide array of economic indicators.

## Data Description
The FRED-MD dataset is a large and complex dataset that includes a wide range of macroeconomic indicators, including industrial production, inflation, interest rates, and more. The dataset is updated monthly and contains data from 1959 to present.

## Objectives
The objectives of this project are to:
- Learn to handle macroeconomic data and perform necessary transformations
- Apply univariate models to predict key economic indicators
- Fit an ARX model using the FRED-MD dataset
- Produce one-step ahead forecasts for industrial production, inflation, and interest rates
- Evaluate the performance of the forecasts using an MSFE loss function
- Apply expanding windows to assess the accuracy of the forecasts

## Installation and Setup
### Step 1: Extract the Folder
- Extract the folder provided at your desktop.
- **Note**: It is necessary to extract it at the desktop, not in any other folder or file.

### Step 2: Install Python (if not already installed)
- If you don’t have any Python compiler installed, follow this tutorial: [How to Install Python](https://youtu.be/4iUJZEa2xP8?feature=shared)

### Step 3: Open Command Prompt (CMD)
- Open CMD by searching for "cmd" in the Windows search bar.
- Navigate to the desktop by running the command:
  ```sh
  cd Desktop
  ```
- Then navigate to the project folder by running the command:
  ```sh
  cd REPORT
  ```

### Step 4: Install Required Python Packages
- Install the necessary packages by running the following commands:
  ```sh
  pip install pandas matplotlib
  ```

  During the installation, if prompted with "yes or no," type `y` and hit enter.

## Running the Code
### Step 5: Run the Python Script
- Go to the `REPORT` folder on the desktop.
- Open the file named `report1.py` in Visual Studio Code (VS Code).
- Click the run button on the upper bar and select "Run without debugging."
- The graph will pop up on the screen as output.

### Additional Information
- The current file used for representation in the graph can be replaced with another file from the [Federal Reserve Bank of St. Louis](https://www.stlouisfed.org). Some minor code changes may be necessary for compatibility.

## Output and Results
The output of the code will include:
- Plots of the transformed data for series like industrial production (INDPRO), inflation (CPIAUCSL), and federal funds rate (TB3MS).
- Graphical representation of the data transformation process.
- Prepared data for fitting an ARX model.

## Troubleshooting and Known Issues
### Common Issues and Solutions
- **Error Messages**: Check for any error messages in the output and consult the documentation for the relevant package or module.
- **Data Loading Issues**: Ensure that you have installed the necessary packages and that the data files are correctly formatted.
- **Model Fitting Issues**: Verify that your model specification is correct and that your data is correctly transformed.

For more details and in-depth troubleshooting, refer to the official documentation of the respective Python packages used in this project.
