# Weather Data Analyzer
# PS No. 89 | First Semester Python Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = "weather.csv"


def load_weather_data():
    """Load weather data from the CSV file."""
    try:
        data = pd.read_csv(FILE_NAME)
        print("\nWeather data loaded successfully!\n")
        print(data.to_string(index=False))
        return data
    except FileNotFoundError:
        print(f"Error: File '{FILE_NAME}' not found. Please enter a valid file name.")
        return None
    except Exception as error:
        print("Error while reading the file:", error)
        return None


def clean_weather_data(data):
    """Remove duplicate rows and fill missing numeric values."""
    if data is None:
        return None

    # Make sure the required columns are present
    required_columns = ["Date", "Temp", "Humidity", "Rainfall"]
    for column in required_columns:
        if column not in data.columns:
            print("Error: CSV file must contain these columns:", required_columns)
            return None

    data = data.copy()

    # Convert weather values to numbers; invalid values become missing values
    for column in ["Temp", "Humidity", "Rainfall"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Remove rows that are exact duplicates
    old_row_count = len(data)
    data = data.drop_duplicates()
    duplicates_removed = old_row_count - len(data)

    # Fill missing values with the mean of each column
    for column in ["Temp", "Humidity", "Rainfall"]:
        if data[column].isna().any():
            if data[column].notna().any():
                column_mean = data[column].mean()
                data[column] = data[column].fillna(column_mean)
            else:
                data[column] = data[column].fillna(0)

    # Remove rows without a date
    data = data.dropna(subset=["Date"])
    data["Date"] = data["Date"].astype(str)

    print("\nData cleaning completed.")
    print("Duplicates removed:", duplicates_removed)
    print("Cleaned rows:", len(data))
    if "Temp" in data.columns:
        print("Missing Temp values filled using mean where needed.")
    print("\nCleaned data:\n")
    print(data.to_string(index=False))

    return data


def show_summary(data):
    """Display basic statistics about the weather."""
    if data is None or data.empty:
        print("No data available for summary.")
        return

    average_temp = np.mean(data["Temp"])
    maximum_temp = data["Temp"].max()
    minimum_temp = data["Temp"].min()
    standard_deviation = np.std(data["Temp"], ddof=0)
    total_rainfall = data["Rainfall"].sum()

    hottest_row = data.loc[data["Temp"].idxmax()]
    coldest_row = data.loc[data["Temp"].idxmin()]

    print("\n========== WEATHER SUMMARY ==========")
    print(f"Average Temp: {average_temp:.2f} C")
    print(f"Max Temp: {maximum_temp:g} C ({hottest_row['Date']})")
    print(f"Min Temp: {minimum_temp:g} C ({coldest_row['Date']})")
    print(f"Standard Deviation: {standard_deviation:.2f}")
    print(f"Total Rainfall: {total_rainfall:g} mm")
    print("=====================================")


def plot_weather(data):
    """Show a temperature line chart and a rainfall bar chart."""
    if data is None or data.empty:
        print("No data available for charts.")
        return

    # Chart 1: Temperature line chart
    plt.figure(figsize=(8, 4))
    plt.plot(data["Date"], data["Temp"], marker="o")
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # Chart 2: Rainfall bar chart
    plt.figure(figsize=(8, 4))
    plt.bar(data["Date"], data["Rainfall"])
    plt.title("Daily Rainfall")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def main():
    print("================================")
    print("       WEATHER DATA ANALYZER")
    print("================================")

    data = load_weather_data()
    if data is None:
        return

    while True:
        print("\nChoose an option:")
        print("1. Show weather summary")
        print("2. Clean data and show charts")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            clean_data = clean_weather_data(data)
            show_summary(clean_data)
        elif choice == "2":
            clean_data = clean_weather_data(data)
            plot_weather(clean_data)
        elif choice == "3":
            print("Thank you for using Weather Data Analyzer!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
