-- Script that creates a view need_meeting that lists all students
-- who have a score under 80 and no last_meeting or more than 1 month

-- Create view need_meeting
CREATE VIEW need_meeting AS
SELECT name
    FROM students
    WHERE score < 80
    AND (last_meeting IS NULL OR last_meeting < SUBDATE(CURDATE(), INTERVAL 1 MONTH));

