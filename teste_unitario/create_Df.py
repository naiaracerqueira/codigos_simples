from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, StructType, TimestampType
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

# data = [('James', '45'), ('Naiara', '36'), ('Pedro', '30')]
# schema = StructType([
#     StructField('_c0', StringType(), True),
#     StructField('_c1', StringType(), True)
# ])
# df = spark.createDataFrame(data, schema)
# df.show()


# data = [("A bola 312-31831 nao sei A"), ("A bola 312-31831 nao sei A")]
# schema = StructType([StructField('value', StringType(), True)])
# df = spark.createDataFrame(data, StringType())
# df.show()


data = [('James', datetime(2020,2,2,23,0,0), None), ('Naiara', datetime(2022,2,2,23,0,0), datetime(2024,1,1,23,0,0)), ('Pedro', None, datetime(2021,1,1,23,0,0))]
schema = StructType([
    StructField('Nome', StringType(), True),
    StructField('Cria', TimestampType(), True),
    StructField('Atua', TimestampType(), True)
])
df = spark.createDataFrame(data, schema)
df.show()

df = df.withColumn('anomesdia', F.coalesce(df.Atua, df.Cria))
df.show()
