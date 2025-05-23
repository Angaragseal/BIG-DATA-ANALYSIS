# BIG-DATA-ANALYSIS

**COMPANY**: CODTECH IT SOLUTIONS  
**NAME**: ANGARAG SEAL  
**INTERN ID**: CT04DN666  
**DOMAIN**: DATA ANALYTICS  
**DURATION**: 4 WEEKS  
**MENTOR**: NEELA SANTOSH

---

## Big Data Analysis of Taxi Trips Using PySpark and Matplotlib

In this project, we conducted a big data analysis on a sample taxi trips dataset using Apache Spark through its Python API (PySpark), and visualized the results using Matplotlib. The objective of the project was to demonstrate scalable data processing using distributed computing tools, along with insightful visualizations that help uncover trends and patterns in taxi service usage.

---

## Project Objectives

- Perform distributed data processing using PySpark.
- Compute aggregated metrics like average fare and distance per passenger count.
- Analyze trip frequency by time (hour of the day).
- Extract and display key trip attributes such as pickup and dropoff location IDs, distance, and fare.
- Visualize findings using Matplotlib for better interpretation and decision-making.

---

## Technologies Used

- **Apache Spark (PySpark)** – High-performance distributed data processing.
- **Python** – Scripting base language.
- **Matplotlib** – For static and interactive visualizations.
- **JDK** – Required for Spark backend.
- **PyCharm** – IDE used for development.

---

## Dataset and Schema

The dataset used is a small sample with fields like:

- Pickup and Dropoff Location IDs
- Trip Distance
- Fare Amount
- Passenger Count
- Pickup Hour

Although the dataset is minimal (only 2 records), the system is scalable for millions of rows using Spark’s parallel computation.

---

## Data Processing Steps

1. **Spark Session Initialization**  
   A Spark session is initialized to work with DataFrames and Spark SQL.

2. **Data Loading**  
   A hardcoded list of taxi trips is converted to an RDD and then to a DataFrame.

3. **Data Aggregation**  
   - Grouped by `passenger_count` to compute average distance and fare.  
   - Grouped by `pickup hour` to analyze peak travel times.

4. **Data Display**  
   Results like average fare by passenger count and trips per hour are displayed using `.show()`.

5. **Visualization**  
   - **Bar Plot**: Average fare per passenger count  
   - **Line Plot**: Number of trips per hour  

   Plots are styled with gridlines, labels, and titles for clarity.

---

## Challenges and Solutions

- **Java gateway process exited**: Fixed by setting `JAVA_HOME`.
- **winutils.exe warning**: Solved by downloading it and setting `HADOOP_HOME`.

---

## Significance of the Project

- PySpark efficiently processes large transportation data.
- Reveals insights like how fares vary by passenger count and trip distance.
- Helps understand travel demand variations across the day.
- Combines scalable processing with strong visual storytelling.

---

## Future Work

- Integrate real-world datasets (e.g., NYC Taxi data).
- Add streaming support with Spark Streaming.
- Enhance visuals using Seaborn or Plotly.
- Add predictive analytics (e.g., fare or duration estimation).

---

## Conclusion

This project demonstrates foundational big data processing using PySpark. It’s scalable, insightful, and ready for real-world applications in industries dealing with high-volume transactional data.

---

##Output
![Image](https://github.com/user-attachments/assets/a69c989d-0152-4aaa-9816-63df69027aca)
![Image](https://github.com/user-attachments/assets/91d4e16b-b473-4bdf-8154-1178cb26063e)
![Image](https://github.com/user-attachments/assets/ae4db39b-b721-4c9d-b7e5-fa2858e19772)
![Image](https://github.com/user-attachments/assets/fcddb964-0ef4-4fb5-ac36-05424f78f314)
![Image](https://github.com/user-attachments/assets/e439e0e7-b4cd-4c34-8ece-3fc150dd8408)
