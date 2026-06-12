-- Script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed

-- Create trigger to validate or reset email validation status before update
DELIMITER $$

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;

