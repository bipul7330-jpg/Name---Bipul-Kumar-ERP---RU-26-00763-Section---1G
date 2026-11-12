WEATHER DATA ANALYZER - PS NO. 89
Python 3 | First Semester Project

FILES
- weather_analyzer.py: main Python program
- weather.csv: sample data
- requirements.txt: required libraries

HOW TO RUN IN VS CODE (Mac)
1. Extract this ZIP file.
2. Open the Weather_Data_Analyzer folder in VS Code.
3. Open Terminal in VS Code (Terminal > New Terminal).
4. Check Python: python3 --version
5. Install libraries once:
   python3 -m pip install -r requirements.txt
6. Run the project:
   python3 weather_analyzer.py
7. Choose:
   1 = weather summary
   2 = clean data and show charts
   3 = exit

CSV COLUMNS
Date, Temp, Humidity, Rainfall

NOTES
- Keep weather.csv and weather_analyzer.py in the same folder.
- If the terminal says a library is missing, run the install command again.
- Option 1 cleans the data before calculating statistics.
- The sample CSV intentionally has a duplicate row and missing temperatures
  so the data-cleaning feature can be demonstrated.
