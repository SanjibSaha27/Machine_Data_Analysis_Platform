**Components of the Platform**

**1. Simulated Sensor Data Generation:**
Simulates machinery sensor data (e.g., temperature, pressure, and vibration levels).

**2. SQL Database:**
Stores sensor data using SQLite for simplicity.

**3. Data Analytics:**
Python script fetches data from the database and processes it for patterns.

**4. Visualization:**
Generates visualizations (using Matplotlib/Seaborn) for operational insights.

**5. Automated Report Generation:**
Exports data summaries and plots to a PDF report.



**Explanation**
Simulated Data:
Random values for temperature, pressure, and vibration simulate real-world sensor readings.

**Database:**
Data is stored in an SQLite database with columns for timestamp, temperature, pressure, and vibration.

**Analysis:**
Data is fetched and analyzed using Pandas.
Summary statistics like mean, standard deviation, and percentiles are calculated.

**Visualization:**
Time series trends for temperature, pressure, and vibration are plotted using Matplotlib.
The plot is saved as an image (sensor_trends.png).

**Automated Report:**
FPDF is used to create a PDF report containing:
Summary statistics.
Sensor data trend visualization.



**Expected Output**
-**SQLite Database:** Stores 100 rows of simulated sensor data.

-**Console Output**: Displays fetched data and summary statistics.

**-Plots:** Line plots for temperature, pressure, and vibration trends.

-**PDF Report:** Machine_Data_Analysis_Report.pdf with analysis and visualization.
