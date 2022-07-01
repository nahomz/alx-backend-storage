-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
SELECT DISTINCT `band_name`,
                IFNULL(`split`, YEAR(CURRENT_DATE())) - `formed` as `lifespan`
    ORDER BY `lifespan` DESC;
