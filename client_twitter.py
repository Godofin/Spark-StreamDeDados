from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder.appName("SparkStreammingTwitter").getOrCreate()

lines = spark.readStream\
    .format("socket")\
    .option("host", "localhost")\
    .option("port", 9009)\
    .load()
words = lines.select(f.explode(f.split(lines.value, ' ')).alias('word'))

wordsCounts = words.groupBy('word').count()

query = wordsCounts.writeStream\
    .outputMode("complete")\
    .format("console")\
    .start()

query.awaitTermination()