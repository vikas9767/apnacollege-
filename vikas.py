from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("sample").getOrCreate()
df = spark.read.csv(r"C:\Users\hP\Desktop\Projectgit\apnacollege-\sample\coustomer.csv").show()