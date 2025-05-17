CREATE TABLE IF NOT EXISTS masters
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone_number TEXT NOT NULL
);
