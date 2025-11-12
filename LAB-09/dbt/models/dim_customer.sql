{{ config(materialized='table') }}

SELECT
  customerNumber AS customer_key,
  customerName,
  contactFirstName,
  contactLastName,
  phone,
  city,
  state,
  postalCode,
  country
FROM {{ source('SALES_SCHEMA', 'CUSTOMERS') }}
