SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY LIKE '인문' 
AND YEAR(PUBLISHED_DATE)=2021 
ORDER BY PUBLISHED_DATE ASC;