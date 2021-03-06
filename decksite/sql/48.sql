CREATE TABLE IF NOT EXISTS rule (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  archetype_id INTEGER NOT NULL,
  FOREIGN KEY(archetype_id) REFERENCES archetype(id) ON DELETE CASCADE ON UPDATE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rule_card (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  rule_id INTEGER NOT NULL,
  card VARCHAR(190) NOT NULL,
  include INTEGER NOT NULL,
  FOREIGN KEY(rule_id) REFERENCES rule(id) ON DELETE CASCADE ON UPDATE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
