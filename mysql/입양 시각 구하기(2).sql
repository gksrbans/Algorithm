WITH RECURSIVE HOUR AS
(
    SELECT 0 AS num
    UNION
    SELECT num+1 AS num FROM HOUR WHERE num<23
)

-- SELECT * FROM HOUR;

SELECT num, COUNT(ANIMAL_ID) FROM HOUR LEFT JOIN ANIMAL_OUTS ON HOUR.num = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR.num