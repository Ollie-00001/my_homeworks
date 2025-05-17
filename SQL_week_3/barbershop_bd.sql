CREATE TABLE IF NOT EXISTS masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone_number TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    price INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('pending', 'completed', 'canceled')),
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS masters_services (
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS appointments_services (
    appointment_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO masters (first_name, last_name, middle_name, phone_number) 
VALUES ('Аркадий', 'Гелев', 'Барберович', '+79001234567');

INSERT INTO masters (first_name, last_name, middle_name, phone)
VALUES ('Левон', 'Бритвич', 'Стригулин', '+79002223344');

