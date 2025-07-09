-- Create the database
CREATE DATABASE IF NOT EXISTS brares_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE brares_db;

-- User for the app (optional, if not already created)
CREATE USER IF NOT EXISTS 'brares'@'localhost' IDENTIFIED BY 'YJXcVV';
GRANT ALL PRIVILEGES ON brares_db.* TO 'brares'@'localhost';
FLUSH PRIVILEGES;

-- Table: UserManagement (for maintenance login)
CREATE TABLE IF NOT EXISTS UserManagement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Table: Director
CREATE TABLE IF NOT EXISTS Director (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_date VARCHAR(100) NOT NULL,
    debut_year INT NOT NULL
);

-- Table: Actor
CREATE TABLE IF NOT EXISTS Actor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_date VARCHAR(100) NOT NULL,
    debut_year INT NOT NULL
);

-- Table: Producer
CREATE TABLE IF NOT EXISTS Producer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_date VARCHAR(100) NOT NULL,
    debut_year INT NOT NULL
);

-- Table: VisualEntertainment (for movies, series, documentaries)
CREATE TABLE IF NOT EXISTS VisualEntertainment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    studio VARCHAR(100) NOT NULL,
    release_year INT NOT NULL,
    seasons INT,
    end_year INT,
    runtime INT,
    rating VARCHAR(10),
    topic VARCHAR(100),
    research_body VARCHAR(100)
);

-- Table: People (for search queries)
CREATE TABLE IF NOT EXISTS People (
    pid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    awards VARCHAR(255),
    experience VARCHAR(255)
);

-- Table: Features (links People to VisualEntertainment with a role)
CREATE TABLE IF NOT EXISTS Features (
    fid INT AUTO_INCREMENT PRIMARY KEY,
    pid INT NOT NULL,
    vid INT NOT NULL,
    role VARCHAR(100) NOT NULL,
    FOREIGN KEY (pid) REFERENCES People(pid) ON DELETE CASCADE,
    FOREIGN KEY (vid) REFERENCES VisualEntertainment(id) ON DELETE CASCADE
);

-- Add some example data for maintenance login
INSERT INTO UserManagement (username, password) VALUES ('admin', 'adminpass'); 