-- Script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for a student

-- Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_avg FLOAT DEFAULT 0;

    -- Calculate the sum of (score * weight) and the sum of weights
    SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_weighted_score, total_weight
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = user_id;

    -- Compute the weighted average if total_weight is greater than 0
    IF total_weight > 0 THEN
        SET weighted_avg = total_weighted_score / total_weight;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users
        SET average_score = weighted_avg
        WHERE id = user_id;
END$$

DELIMITER ;

