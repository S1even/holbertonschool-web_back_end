-- Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students

-- Create stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update average_score for all users using a joined aggregated subquery
    UPDATE users AS u
    JOIN (
        SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight) AS weighted_avg
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS score_data ON u.id = score_data.user_id
    SET u.average_score = score_data.weighted_avg;
END$$

DELIMITER ;

