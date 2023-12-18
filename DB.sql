.open project.db

CREATE TABLE topics
(
	topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL
);

CREATE TABLE quotes
(
	quote_id INTEGER PRIMARY KEY AUTOINCREMENT,
	topic INTEGER DEFAULT 0,
	quote TEXT NOT NULL,
	author TEXT,
	rating INTEGER DEFAULT 0 CHECK (rating > -1 AND rating < 6),
	favourite INTEGER DEFAULT 0 CHECK (favourite > -1 AND favourite < 2)
);