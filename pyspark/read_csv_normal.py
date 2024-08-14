from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from datetime import datetime

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("delimiter", ";").csv('pyspark/teste_csv_normal.csv', header=True)
df.show()

df = df.withColumn('data', F.to_timestamp(F.col('data'), 'yyyy-MM-dd-HH.mm.ss.SSSSSS'))
df.show(truncate = False)

last_execution = datetime(2024,4,1)
df = df.filter(F.col('data') > F.lit(last_execution))
df.select('data').show()

