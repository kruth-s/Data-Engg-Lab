{{ config(materialized='table') }}

SELECT
  employeeNumber AS employee_key,
  firstName,
  lastName,
  email,
  jobTitle,
  officeCode
FROM {{ source('SALES_SCHEMA', 'EMPLOYEES') }}
