PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS barbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL CHECK(price >= 0)
);

CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    barber_id INTEGER NOT NULL,
    comment TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (barber_id) REFERENCES barbers(id)
);

CREATE TABLE IF NOT EXISTS appointments_services (
    appointment_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

INSERT INTO barbers (name) VALUES ('Аркадий'), ('Игорь'), ('Степан');
INSERT INTO services (name, price) VALUES ('Стрижка', 2200), ('Бритьё', 1500), ('Укладка', 500);
INSERT INTO clients (name, phone) VALUES ('Егор', '89991112233'), ('Олег', '89991114455');

INSERT INTO appointments (client_id, barber_id, comment)
VALUES (1, 1, 'Очень вежливый клиент'), (2, 2, 'Просил намутить стилёчек');

INSERT INTO appointments_services (appointment_id, service_id)
VALUES (1, 1), (1, 3), (2, 2);

CREATE INDEX idx_clients_phone ON clients (phone);

CREATE INDEX idx_appointments_barbers_date ON appointments (barber_id, created_at);

CREATE INDEX idx_appointments_comment ON appointments (comment);

CREATE INDEX idx_appointments_services_id ON appointments_services(service_id, appointment_id);

COMMIT;
PRAGMA foreign_keys = ON;