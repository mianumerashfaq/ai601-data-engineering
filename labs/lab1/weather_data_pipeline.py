import requests
import csv

URL = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

### Part 1. Read Operation (Extract)
def fetch_weather_data():
    """Fetches weather data for the past 10 days."""
    #response = requests.get(URL,params={"past_days": 10})
    response = requests.get(URL + "&past_days=10")
    print(response.json())

### Part 2. Write Operation (Load)
def save_to_csv(data, filename):
    """Saves weather data to a CSV file."""
    with open(filename, "w", newline='', encoding='utf-8') as file:
        ### TODO: complete rest of the code, HINT: write the header row and body separately
        writer = csv.writer(file)
        timestamps = data["hourly"]["time"]  # Extract timestamps
        temperatures = data["hourly"]["temperature_2m"]  # Extract temperature values
        humidity=data["hourly"]["relative_humidity_2m"]
        windspeed=data["hourly"]["wind_speed_10m"]
            
        # Write the header row
        writer.writerow(["Timestamp", "Temperature (°C)","humidity","windspeed"])

        # Write the data rows
        for timestamp, temp in zip(timestamps, temperatures,humidity,windspeed):
            writer.writerow([timestamp, temp,humid,wind])
        
        return None

### Part 3. Cleaning Operation (Transform)
def clean_data(input_file, output_file):
    """ clean the data based on the following rules:
        1. Temperature should be between 0 and 60°C
        2. Humidity should be between 0% and 80%
        3. Wind speed in a betweeen 3 and 150
    """

    ### TODO: complete rest of the code
            
    print("Cleaned data saved to", output_file)

### Part 4. Aggregation Operation 
def summarize_data(filename):
    """Summarizes weather data including averages and extremes."""
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read header row
        data = list(reader)  # Convert CSV data to list

        # Ensure we have data
        if not data:
            print("No data available to summarize.")
            return

        # Extract values from columns
        temperatures = [float(row[1]) for row in data if row[1]]
        humidity_values = [float(row[2]) for row in data if row[2]]
        wind_speeds = [float(row[3]) for row in data if row[3]]

        # Compute statistics
        ### TODO: complete rest of the code by computing the below mentioned metrics

        # Print summary
        print("📊 Weather Data Summary 📊")
        print(f"Total Records: {total_records}")
        print(f"🌡️ Average Temperature: {avg_temp:.2f}°C")
        print(f"🔥 Max Temperature: {max_temp:.2f}°C")
        print(f"❄️ Min Temperature: {min_temp:.2f}°C")
        print(f"💧 Average Humidity: {avg_humidity:.1f}%")
        print(f"💨 Average Wind Speed: {avg_wind_speed:.2f} m/s")


if __name__ == "__main__":
    weather_data = fetch_weather_data()
    
    save_to_csv(weather_data, "weather_data.csv")
    print(f"CSV file '{"weather_data.csv"}' has been saved successfully.")
        #clean_data("weather_data.csv", "cleaned_data.csv")
        #print("Weather data clean saved to cleaned_data.csv")
        #summarize_data("cleaned_data.csv")
    #weather_data()
        

