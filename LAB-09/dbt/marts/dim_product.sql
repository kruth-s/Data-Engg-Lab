{{ config(materialized='table') }}

SELECT
  productCode AS product_key,
  productName,
  productLine,
  productScale,
  productVendor,
  quantityInStock,
  buyPrice,
  MSRP
FROM {{ source('SALES_SCHEMA', 'PRODUCTS') }}
