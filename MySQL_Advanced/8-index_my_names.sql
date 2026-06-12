-- Script that creates an index idx_name_first on the table names
-- The index only targets the first letter of the name column

-- Create prefix index on the first character of the name column
CREATE INDEX idx_name_first ON names (name(1));

