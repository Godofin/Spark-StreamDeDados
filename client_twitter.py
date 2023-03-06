from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkStreammingTwitter").getOrCreate()

lines = spark.readStream\
    .format("socket")\
    .option("host", "localhost")\
    .option("port", 9009)\
    .load()

query = lines.writeStream\
    .outputMode("append")\
    .format("console")\
    .start()

query.awaitTermination()