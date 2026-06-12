-- Script that lists all bands with Glam rock as their main style
-- Ranked by their longevity up to the year 2024

-- Select band name and compute lifespan based on formed and split years
SELECT band_name, 
       (IF(split = '?' OR split IS NULL, 2024, CAST(split AS SIGNED)) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;

