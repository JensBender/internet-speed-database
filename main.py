# Import modules
from speedtest import SpeedtestBot
from google_forms import GoogleFormsBot

# Create a speedtest bot
speedtest_bot = SpeedtestBot()
# Run a speedtest to get download speed, upload speed, and internet provider
speedtest_bot.run_speedtest()
# Print results
print(f"Download speed: {speedtest_bot.down} Mbps")
print(f"Upload speed: {speedtest_bot.up} Mbps")
print(f"Internet provider: {speedtest_bot.provider}")

# Create a Google forms bot
google_forms_bot = GoogleFormsBot()
# Fill out the form with the information from the speedtest
google_forms_bot.fill_out_form(speedtest_bot.down, speedtest_bot.up, speedtest_bot.provider)
