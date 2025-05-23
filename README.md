# BIG-DATA-ANALYSIS
*COMPANY*: CODTECH IT SOLUTIONS
*NAME*: ANGARAG SEAL
*INTERN ID*: CT04DN666
*DOMAIN*: DATA ANALYTICS
*DURATION*: 4 WEEKS
*MENTOR*: NEELA SANTOSH

Big Data Analysis of Taxi Trips Using PySpark and Matplotlib:
In this project, we conducted a big data analysis on a sample taxi trips dataset using Apache Spark through its Python API (PySpark), and visualized the results using Matplotlib. The objective of the project was to demonstrate scalable data processing using distributed computing tools, along with insightful visualizations that help uncover trends and patterns in taxi service usage.

Project Objectives:
The key goals of this project were:
To perform distributed data processing using PySpark.
To compute aggregated metrics like average fare and distance per passenger count.
To analyze trip frequency by time (hour of the day).
To extract and display key trip attributes such as pickup and dropoff location IDs, distance, and fare.
To visualize findings using Matplotlib for better interpretation and decision-making.

Technologies Used:
Apache Spark (PySpark): Used for high-performance distributed data processing.
Python: General-purpose programming language used as the scripting base.
Matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python.
JDK (Java Development Kit): Required for Spark backend operations.
PyCharm: Python IDE used for development.

Dataset and Schema:
The dataset used is a small sample containing trip records with fields like:
Pickup and Dropoff Location IDs
Trip Distance
Fare Amount
Passenger Count
Pickup Hour
Although the sample dataset used here is synthetic and minimal (only two records for demonstration), the system is built to handle large-scale data (e.g., millions of rows) using Spark’s parallel computation capabilities.

Data Processing Steps:
Spark Session Initialization:
A Spark session is initialized which acts as the entry point for working with DataFrames and Spark SQL.
Data Loading:
A hardcoded list of sample taxi trip records is parallelized into an RDD and then converted into a DataFrame with appropriate schema fields.
Data Aggregation:
First, the data is grouped by passenger_count to calculate average trip distance and fare.
Next, trip counts are grouped by pickup hour to identify peak times of travel.
Data Display:
The computed results such as average fare by passenger count and number of trips per hour are displayed using show() methods for verification and transparency.
Visualization:
Two different plots were created using Matplotlib:
Bar Plot: Depicting average fare for each passenger count, offering insight into how fare trends change with group size.
Line Plot: Showing number of trips per hour, helping us understand rush hours or periods of high activity.
The program includes adjustments to ensure both plots are displayed one after the other correctly. Plot aesthetics are handled to improve readability (e.g., gridlines, labels, and titles).

Challenges and Solutions:
One of the initial challenges encountered was the “Java gateway process exited before sending its port number” error. This was due to improper Java environment configuration. It was resolved by correctly setting the JAVA_HOME environment variable to the JDK path.
Another warning message about winutils.exe was resolved by downloading the required binary and setting the HADOOP_HOME variable. These setup steps were crucial to ensure the Spark context could initialize correctly on a Windows environment.

Significance of the Project:
This project demonstrates how PySpark can be effectively used to process and analyze large-scale transportation data. It shows how simple transformations and aggregations can reveal important insights, such as:
The average fare tends to increase with trip distance and number of passengers.
Travel demand varies throughout the day, which can help with operational planning for taxi services.
By combining PySpark’s power with Matplotlib’s visualization capabilities, the project offers a complete pipeline from raw data ingestion to final insight presentation.

Future Work:
Real-world Dataset Integration: Integrate larger CSV/Parquet files from NYC Taxi dataset.
Streaming Support: Use Spark Streaming for real-time trip data analysis.
Advanced Visualization: Use seaborn or plotly for interactive charts.
Predictive Analysis: Apply machine learning models (e.g., fare prediction, trip duration estimation).

Conclusion:
This project serves as a foundational demonstration of big data processing with PySpark. It’s highly scalable and provides actionable insights using just a small sample. The combination of distributed processing with clean visualizations makes it a robust and extensible framework for data analysis in any industry dealing with large volumes of transactional data.
