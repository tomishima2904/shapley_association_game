CREATE DATABASE IF NOT EXISTS shapley;
USE shapley;
GRANT ALL ON shapley.* to shapley;
DROP TABLE IF EXISTS words;
CREATE TABLE words(
    qid INT NOT NULL AUTO_INCREMENT,
    answer varchar(20),
    `stimulus_1` varchar(20),
    `stimulus_2` varchar(20),
    `stimulus_3` varchar(20),
    `stimulus_4` varchar(20),
    `stimulus_5` varchar(20),
    PRIMARY KEY (qid)
);
INSERT INTO words (answer, category, `stimulus_1`, `stimulus_2`, `stimulus_3`, `stimulus_4`, `stimulus_5`) VALUES
('スポーツ', 'バレーボール', '水泳', 'マラソン', '体操', 'サッカー'),
('薬', '鎮痛剤', '湿布', 'カプセル', '軟膏', '錠剤');