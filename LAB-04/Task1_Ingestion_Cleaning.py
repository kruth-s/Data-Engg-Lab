from pyspark.sql.functions import col, to_date

df_raw = spark.table("ecommerce_orders")

df_cleaned = (

df_raw.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))

.withColumn("total_value", col("quantity") * col("price"))

)

# Save as a managed Silver table

df_cleaned.createOrReplaceTempView("tmp_ecommerce_orders_cleaned")

spark.sql("""

CREATE OR REPLACE TABLE silver_ecommerce_orders AS

SELECT * FROM tmp_ecommerce_orders_cleaned

""")