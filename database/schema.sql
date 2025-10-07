CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    level VARCHAR(10),
    component VARCHAR(50),
    message TEXT
);
