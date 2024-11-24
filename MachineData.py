import sqlite3
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Simulate sensor data and store it in a SQLite database
def generate_sensor_data():
    # Simulate sensor readings for a machine
    temperature = random.uniform(20.0, 80.0)  # °C
    pressure = random.uniform(10.0, 100.0)    # PSI
    vibration = random.uniform(0.1, 5.0)      # mm/s
    return temperature, pressure, vibration

# Create SQLite database and table
def setup_database():
    conn = sqlite3.connect('machine_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            pressure REAL,
            vibration REAL
        )
    ''')
    conn.commit()
    conn.close()

# Insert data into the database
def insert_data(temperature, pressure, vibration):
    conn = sqlite3.connect('machine_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (timestamp, temperature, pressure, vibration)
        VALUES (datetime('now'), ?, ?, ?)
    ''', (temperature, pressure, vibration))
    conn.commit()
    conn.close()

# Generate data continuously (optional)
def generate_and_store_data(iterations=10, interval=1):
    for _ in range(iterations):
        temp, pres, vib = generate_sensor_data()
        insert_data(temp, pres, vib)
        time.sleep(interval)

# Analyze data
def fetch_and_analyze_data():
    conn = sqlite3.connect('machine_data.db')
    query = 'SELECT * FROM sensor_data'
    df = pd.read_sql_query(query, conn)
    conn.close()
    print("Fetched Data:\n", df.head())
    
    # Analysis: Summary statistics
    summary = df.describe()
    print("\nSummary Statistics:\n", summary)
    
    return df, summary

# Visualize data
def create_visualizations(df):
    # Plot temperature, pressure, and vibration
    plt.figure(figsize=(12, 6))
    
    # Temperature trend
    plt.subplot(3, 1, 1)
    plt.plot(df['timestamp'], df['temperature'], label='Temperature', color='red')
    plt.ylabel('Temperature (°C)')
    plt.title('Sensor Data Trends')
    plt.legend()
    
    # Pressure trend
    plt.subplot(3, 1, 2)
    plt.plot(df['timestamp'], df['pressure'], label='Pressure', color='blue')
    plt.ylabel('Pressure (PSI)')
    plt.legend()
    
    # Vibration trend
    plt.subplot(3, 1, 3)
    plt.plot(df['timestamp'], df['vibration'], label='Vibration', color='green')
    plt.xlabel('Timestamp')
    plt.ylabel('Vibration (mm/s)')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('sensor_trends.png')  # Save the visualization
    plt.show()

# Generate automated report
def generate_report(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add Title
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Machine Data Analysis Report", ln=True, align='C')
    
    # Add Summary Statistics
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Summary Statistics:", ln=True)
    for col, stats in summary.iteritems():
        pdf.cell(0, 10, txt=f"{col}: {stats}", ln=True)
    
    # Add visualization
    pdf.ln(10)
    pdf.cell(200, 10, txt="Sensor Data Trends:", ln=True)
    pdf.image('sensor_trends.png', x=10, y=None, w=180)
    
    pdf.output("Machine_Data_Analysis_Report.pdf")

# Main Function
if __name__ == "__main__":
    # Setup
    setup_database()
    
    # Generate and store simulated data
    generate_and_store_data(iterations=100, interval=0.1)  # Generate 100 rows quickly
    
    # Analyze the data
    df, summary = fetch_and_analyze_data()
    
    # Visualize the data
    create_visualizations(df)
    
    # Generate automated report
    generate_report(summary)
