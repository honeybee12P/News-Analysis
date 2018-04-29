import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import split
from pyspark.sql import functions as F

sc =SparkContext()
sqlContext = SQLContext(sc)
dataFile = sys.argv[1];
data = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load(dataFile) 

#deleting index column 
data = data.drop('_c0')

#deleting url column as it contains Nan
data = data.drop('url')

#deleting author column as it contains Nan
data = data.drop('author')

#converting year and month which is in decimal format to integer
data=data.withColumn("year", data["year"].cast(IntegerType()))
data = data.filter(data.year != "2011")
data = data.filter(data.year != "2012")
data = data.filter(data.year != "2013")
data = data.filter(data.year != "2014")

data=data.withColumn("month", data["month"].cast(IntegerType()))
data = data.filter(data.month != "2016")
data = data.filter(data.month != "2017")
data.printSchema()

dataNYCTimes2016 = data.filter(data.publication == "New York Times").filter(data.year == 2016).limit(500)
dataNYCTimes2017 = data.filter(data.publication == "New York Times").filter(data.year == 2017).limit(500)
dataNYCTimes = dataNYCTimes2016.union(dataNYCTimes2017)

dataBreitbart2016 = data.filter(data.publication == "Breitbart").filter(data.year == 2016).limit(500)
dataBreitbart2017 = data.filter(data.publication == "Breitbart").filter(data.year == 2017).limit(500)
dataBreitbart = dataBreitbart2016.union(dataBreitbart2017)

dataCNN2016 = data.filter(data.publication == "CNN").filter(data.year == 2016).limit(500)
dataCNN2017 = data.filter(data.publication == "CNN").filter(data.year == 2017).limit(500)
dataCNN = dataCNN2016.union(dataCNN2017)

dataBusinessInsider2016 = data.filter(data.publication == "Business Insider").filter(data.year == 2016).limit(500)
dataBusinessInsider2017 = data.filter(data.publication == "Business Insider").filter(data.year == 2017).limit(500)
dataBusinessInsider = dataBusinessInsider2016.union(dataBusinessInsider2017)

dataAtlantic2016 = data.filter(data.publication == "Atlantic").filter(data.year == 2016).limit(500)
dataAtlantic2017 = data.filter(data.publication == "Atlantic").filter(data.year == 2017).limit(500)
dataAtlantic = dataAtlantic2016.union(dataAtlantic2017)

combinedData1 = dataNYCTimes.union(dataBreitbart)

combinedData2 = combinedData1.union(dataCNN)

combinedData3 = combinedData2.union(dataBusinessInsider)

combinedData4 = combinedData3.union(dataAtlantic)

combinedData4.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save(sys.argv[2])
 

