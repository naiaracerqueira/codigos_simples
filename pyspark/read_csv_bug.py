from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

df = spark.read.text('pyspark/teste_csv_bug.csv')
df.show()

primeira = df.head(1)[0].value
ultima = df.tail(1)[0] .value

df = df.filter(
    (F.col('value') != F.lit(primeira)) & 
    (F.col('value') != F.lit(ultima))
)

df.show()