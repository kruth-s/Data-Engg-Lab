{{ config(materialized='table') }}

SELECT
  o.orderNumber      AS order_id,
  o.orderDate,
  o.status,
  c.customerNumber   AS customer_id,
  p.productCode      AS product_id,
  od.quantityOrdered AS quantity,
  od.priceEach       AS price,
  (od.quantityOrdered * od.priceEach) AS total_amount
FROM {{ source('SALES_SCHEMA', 'ORDERS') }} AS o
JOIN {{ source('SALES_SCHEMA', 'ORDERDETAILS') }} AS od
  ON o.orderNumber = od.orderNumber
JOIN {{ source('SALES_SCHEMA', 'CUSTOMERS') }} AS c
  ON o.customerNumber = c.customerNumber
JOIN {{ source('SALES_SCHEMA', 'PRODUCTS') }} AS p
  ON od.productCode = p.productCode
