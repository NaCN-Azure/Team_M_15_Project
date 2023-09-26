CREATE TABLE bike (
  id INTEGER PRIMARY KEY,
  bike_type TEXT NOT NULL,
  longitude REAL,
  latitude REAL,
  is_broken INTEGER NOT NULL,
  is_use INTEGER,
  city TEXT,
  total_minutes REAL,
  battery INTEGER NOT NULL DEFAULT 100
);

-- order±í 
CREATE TABLE "order" (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  bike_id INTEGER,
  from_longitude REAL,
  to_longitude REAL, 
  from_latitude REAL,
  to_latitude REAL,
  start_date TEXT,
  cost REAL,
  end_date TEXT
);

-- report±í
CREATE TABLE report (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  order_id INTEGER,
  bike_id INTEGER,
  message TEXT,
  problem_type TEXT,
  is_solved INTEGER,
  city TEXT
);

-- user±í
CREATE TABLE user (
  id INTEGER PRIMARY KEY,
  user_name TEXT NOT NULL,
  email TEXT NOT NULL, 
  phone TEXT NOT NULL,
  birthday TEXT NOT NULL,
  user_type TEXT NOT NULL,
  wallet REAL NOT NULL,
  city TEXT NOT NULL,
  password TEXT,
  salt TEXT
);

INSERT INTO user VALUES (1,'Tom','123@gmail.com','0466222511','2001/02/25','0',188.36,'Glasgow','123456',NULL);