-- Script that creates a function SafeDiv that divides two numbers
-- It returns the result of the division, or 0 if the second number is 0

-- Create function SafeDiv
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Check if the denominator is zero
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$

DELIMITER ;

