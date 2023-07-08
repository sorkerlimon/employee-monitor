import mysql.connector

def login(username, password):
    try:
        # Connect to the database
        cnx = mysql.connector.connect(
            host='192.168.100.25',
            port=3306,  # Specify the port number here
            user='iimi',
            password='limon@123',
            database='workflow'
        )

        cursor = cnx.cursor()

        # Execute the query
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch the result
        result = cursor.fetchone()

        if result is not None:
            print("Login successful")
        else:
            print("Invalid username or password")

        # Close the database connection
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(f"Failed to connect to the database: {err}")

# Usage example
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)


# CREATE USER 'iimi'@'192.168.100.250' IDENTIFIED BY 'limon@123';
# GRANT ALL PRIVILEGES ON *.* TO 'iimi'@'192.168.100.250';
# FLUSH PRIVILEGES;
# SELECT host FROM mysql.user WHERE user = "iimi";


# CREATE TABLE users (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   username VARCHAR(255) NOT NULL,
#   password VARCHAR(255) NOT NULL
# );

# CREATE TABLE ip_time (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   user_id INT,
#   local_ip_address VARCHAR(255),
#   public_ip_address VARCHAR(255),
#   physical_address VARCHAR(255),
#   start_time VARCHAR(50),
#   close_time VARCHAR(50),
#   FOREIGN KEY (user_id) REFERENCES users(id)
# );
