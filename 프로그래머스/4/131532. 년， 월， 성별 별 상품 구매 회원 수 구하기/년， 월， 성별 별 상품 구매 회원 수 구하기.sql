-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, GENDER, COUNT(DISTINCT o.USER_ID) as USERS
FROM USER_INFO as u JOIN ONLINE_SALE as o
ON u.USER_ID = o.USER_ID
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
HAVING GENDER IS NOT NULL
ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER;