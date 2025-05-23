from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName("BigDataAnalysis").getOrCreate()

# Sample Data: (pickup_location_id, dropoff_location_id, passenger_count, trip_distance, fare_amount, hour)
data = [
    (101, 201, 1, 2.5, 10.0, 8),
    (102, 202, 2, 5.1, 20.0, 14),
    (103, 203, 3, 7.8, 35.0, 9),
    (101, 204, 1, 3.2, 15.0, 8),
    (104, 205, 4, 12.5, 50.0, 17),
    (102, 206, 2, 4.0, 18.0, 14),
    (101, 201, 1, 6.7, 25.0, 8)
]

columns = ["pickup_location_id", "dropoff_location_id", "passenger_count", "trip_distance", "fare_amount", "hour"]

df = spark.createDataFrame(data, schema=columns)

# Basic Aggregations
agg_df = df.groupBy("passenger_count").agg(
    count("*").alias("trip_count"),
    avg("trip_distance").alias("avg_distance"),
    avg("fare_amount").alias("avg_fare"),
    max("fare_amount").alias("max_fare"),
    min("fare_amount").alias("min_fare")
).orderBy("passenger_count")

agg_df.show()

# Trips per hour
trips_by_hour = df.groupBy("hour").count().orderBy("hour")
trips_by_hour.show()

# Filter trips with distance > 5
long_trips = df.filter(df.trip_distance > 5)
long_trips.show()

# Export to Pandas for plotting
pandas_agg = agg_df.toPandas()
pandas_hour = trips_by_hour.toPandas()

# Plot: Average fare by passenger count
plt.figure(figsize=(8,5))
plt.bar(pandas_agg['passenger_count'], pandas_agg['avg_fare'], color='skyblue')
plt.xlabel('Passenger Count')
plt.ylabel('Average Fare')
plt.title('Average Fare by Passenger Count')
plt.grid(axis='y')
plt.show(block=False)
plt.pause(3)  # Pause 3 seconds so plot shows
plt.close()

plt.figure(figsize=(8,5))
plt.plot(pandas_hour['hour'], pandas_hour['count'], marker='o', linestyle='-', color='green')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Trips')
plt.title('Number of Trips per Hour')
plt.grid(True)
plt.show()


spark.stop()
