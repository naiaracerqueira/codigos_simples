from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, StructType


spark = SparkSession.builder.getOrCreate()

# data = [('James', '45'), ('Naiara', '36'), ('Pedro', '30')]
# schema = StructType([
#     StructField('_c0', StringType(), True),
#     StructField('_c1', StringType(), True)
# ])
# df = spark.createDataFrame(data, schema)

# df = spark.createDataFrame(
#     [
#         (1, "foo"),  # create your data here, be consistent in the types.
#         (2, "bar"),
#     ],
#     ["id", "label"]  # add your column names here
# )

# data = [{"_c0": 'c1 | c2 | c3'},
#         {"_c0": 'col1 | col2 | col3'}, 
#         {"_c0": 'cl1 | cl2 | cl3'}
#         ]

data = [{"c0": 'linha1', 
         'c1': '2022-02-01'}]

# data = [{"c0": ['linha1','linha2','linha3'], 
#          'c1': ['linha1','linha2','linha3']}]

df = spark.createDataFrame(data, [StringType(),StringType()])

df.show()