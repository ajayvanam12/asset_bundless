from pyspark import pipelines as dp

@dp.materialized_view(
    name="sales_summary"
)
def sales_summary():
    return spark.sql("""
        SELECT
            product_id,
            SUM(quantity) AS total_quantity,
            SUM(total_amount) AS total_sales,
            AVG(unit_price) AS avg_price
        FROM devs.ansh.sales
        GROUP BY product_id
    """)