import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Step 1: Data Acquisition
# Get data from following link
# url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/02-12-2023.csv"
covid_data = pd.read_csv("covid-sample-data-program-25.csv")

# Step 3: Exploratory Data Analysis (EDA)
covid_data['Date'] = pd.to_datetime(covid_data['Last_Update']).dt.date
daily_new_cases = covid_data.groupby('Date').size().diff().fillna(0)  # Calculate daily new cases
plt.figure(figsize=(10, 6))
plt.plot(daily_new_cases)
plt.title('Daily New COVID-19 Cases Worldwide')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.grid(True)
plt.show()

# Step 4: Statistical Analysis
total_cases = covid_data['Confirmed'].sum()
total_deaths = covid_data['Deaths'].sum()
total_recovered = covid_data['Recovered'].sum()

print("Total Confirmed Cases Worldwide:", total_cases)
print("Total Deaths Worldwide:", total_deaths)
print("Total Recovered Cases Worldwide:", total_recovered)

# Step 5: Modeling
dates = np.arange(len(daily_new_cases)).reshape(-1, 1)
cases = np.array(daily_new_cases).reshape(-1, 1)

slope, intercept, _, _, _ = linregress(dates.flatten(), cases.flatten())
future_dates = np.arange(len(daily_new_cases) + 7).reshape(-1, 1)
predicted_cases = slope * future_dates + intercept

plt.figure(figsize=(10, 6))
plt.plot(dates, cases, label='Actual Daily New Cases')
plt.plot(future_dates, predicted_cases, linestyle='--', color='red', label='Predicted Daily New Cases (Next 7 Days)')
plt.title('Daily New COVID-19 Cases Worldwide and Prediction')
plt.xlabel('Days Since Start')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.show()

# Step 6: Interpretation and Conclusion
print("\nInterpretation and Conclusion:")
print("Based on the linear regression model, the predicted number of new cases for the next 7 days is as follows:")
for i in range(1, 8):
    print(f"Day {i}: {predicted_cases[-1 * (7 - i)][0]:.0f}")

print("\nThe linear regression model suggests a trend in the number of new cases, but it's important to note that various factors can influence the actual number of cases, including public health measures, vaccination rates, and virus mutations.")

