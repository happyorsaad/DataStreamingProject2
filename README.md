***SF Crime Project***

**Question 1**

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

It either increased or decreased processedRowsPerSecond

**Question 2**

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

The options with the most effect was the following, set to the respective values. The meassure I used to guage the effect was processedRowsPerSecond. In Apache Spark, shuffle is one of costliest operation. Effective parallelising of this operation gives good performing for spark jobs. So I changed the following properties. Since we are dealing with a small dataset, 200 is a overkill.

- spark.sql.shuffle.partitions                30
- spark.streaming.kafka.maxRatePerPartition   30
