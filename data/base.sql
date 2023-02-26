CREATE DATABASE IF NOT EXISTS shapley;
USE shapley;
GRANT ALL ON shapley.* to shapley;
DROP TABLE IF EXISTS words;
CREATE TABLE words(
    qid INT NOT NULL AUTO_INCREMENT,
    answer VARCHAR(20),
    category VARCHAR(3),
    `stimulus_1` VARCHAR(20),
    `stimulus_2` VARCHAR(20),
    `stimulus_3` VARCHAR(20),
    `stimulus_4` VARCHAR(20),
    `stimulus_5` VARCHAR(20),
    PRIMARY KEY (qid)
);
INSERT INTO words (answer, `stimulus_1`, `stimulus_2`, `stimulus_3`, `stimulus_4`, `stimulus_5`, category) VALUES