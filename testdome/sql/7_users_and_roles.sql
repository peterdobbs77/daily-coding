--TABLE users
--  id INTEGER NOT NULL PRIMARY KEY,
--  userName VARCHAR(50) NOT NULL
--
--TABLE roles
--  id INTEGER NOT NULL PRIMARY KEY,
--  role VARCHAR(20) NOT NULL


CREATE TABLE users_roles (
  userId INTEGER NOT NULL REFERENCES users(id),
  roleId INTEGER NOT NULL REFERENCES roles(id),
  UNIQUE(userId,roleId)
);
