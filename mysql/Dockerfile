# Use the official MySQL image as a base
FROM mysql:latest

# Environment variables to configure the database (uncomment if you dont use docker-compose)
# ENV MYSQL_ROOT_PASSWORD=root_password
# ENV MYSQL_DATABASE=my_database
# ENV MYSQL_USER=my_user
# ENV MYSQL_PASSWORD=my_password

# Copy the SQL script to initialize the database
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose port 3306 to allow external applications to connect to the database
EXPOSE 3306