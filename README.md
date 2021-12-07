# mysql1
MySQL example course section from LinkedIn course.

###Code to create a new user in the db:
 CREATE USER 'charbel'@'%' IDENTIFIED BY 'pass123';
 
###Grant admin access to db:
GRANT ALL PRIVILEGES ON projects.* to 'charbel'@'%';