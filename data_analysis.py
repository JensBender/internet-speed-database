# Import modules
import requests
import pandas as pd
import your_secrets

# Get data
# Get the Google Sheet data (using Sheety API)
get_sheet_response = requests.get(url=your_secrets.SHEETY_PROJECT_ENDPOINT,
                                  headers={"Authorization": f"Bearer {your_secrets.SHEETY_BEARER_TOKEN}"})
# Save the data as json
google_sheet_json = get_sheet_response.json()
# Convert json to pandas dataframe
speedtest_df = pd.DataFrame(google_sheet_json["responses"])

# Data preparation
# Rename variables
speedtest_df.rename(columns={"downloadSpeed": "Download", "uploadSpeed": "Upload",
                             "internetProvider": "Provider"}, inplace=True)
# Create date variable
speedtest_df["date"] = speedtest_df["timestamp"].str.split(" ", n=1, expand=True)[0]
# Create time variable
speedtest_df["time"] = speedtest_df["timestamp"].str.split(" ", n=1, expand=True)[1]
# Print dataframe
print(speedtest_df.to_string())

# Group the data
# By internet provider
by_provider = speedtest_df.groupby("Provider")

# Data analysis
# Get number of speedtests by provider
count = by_provider.size()
# Get average download speed by provider
down_median = round(by_provider["Download"].median(), 1)
down_mean = round(by_provider["Download"].mean(), 1)
# Get average upload speed by provider
up_median = round(by_provider["Upload"].median(), 1)
up_mean = round(by_provider["Upload"].mean(), 1)
# Create dataframe with number of speedtests, average download, and average upload speed by internet provider
down_up_median = count.to_frame().join(down_median).join(up_median)
down_up_median.rename(columns={0: "n", "Download": "Median Download", "Upload": "Median Upload"}, inplace=True)
down_up_mean = count.to_frame().join(down_mean).join(up_mean)
down_up_mean.rename(columns={0: "n", "Download": "Mean Download", "Upload": "Mean Upload"}, inplace=True)
# Print results
print(down_up_median.to_string())
print(down_up_mean.to_string())
