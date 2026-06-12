-- Script that creates a composite index idx_name_first_score on the table names
-- The index targets the first letter of the name column and the score column

-- Create composite index on the first character of name and the score
CREATE INDEX idx_name_first_score ON names (name(1), score);

