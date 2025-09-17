from pyspark.sql.functions import sum as spark_sum

df_cleaned = spark.table("silver_ecommerce_orders")

# Revenue by product category (Gold layer)

df_category_sales = (

df_cleaned.groupBy("product_category")

.agg(spark_sum("total_value").alias("total_revenue"))

)

df_category_sales.createOrReplaceTempView("tmp_ecommerce_category_sales")

spark.sql("""

CREATE OR REPLACE TABLE gold_ecommerce_category_sales AS

SELECT * FROM tmp_ecommerce_category_sales

""")

df_daily_sales = (

df_cleaned.groupBy("order_date")

.agg(spark_sum("total_value").alias("daily_revenue")) )

df_daily_sales.createOrReplaceTempView("tmp_ecommerce_daily_sales")

spark.sql("""

CREATE OR REPLACE TABLE gold_ecommerce_daily_sales AS

SELECT * FROM tmp_ecommerce_daily_sales

""")