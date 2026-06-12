-- Script that ranks country origins of bands, ordered by the number of fans
-- The script groups by origin and sums up the fans for each country

-- Select origin and the total sum of fans, ordered by the total number of fans
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;

