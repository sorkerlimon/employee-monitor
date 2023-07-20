import mysql.connector
from mysql.connector import Error
import datetime

try:
    # Connect to the database
    connection = mysql.connector.connect(
        host='192.168.100.25',
        port=3306,
        user='iimi',
        password='limon@123',
        database='workflow'
    )

    # Calculate the date for 2 days ago
    two_days_ago = datetime.date.today() - datetime.timedelta(days=2)

    # Create a cursor object
    cursor = connection.cursor()

    # Retrieve the dynamic_data rows for the previous 2 days
    select_dynamic_data_query = "SELECT * FROM dynamic_data WHERE ip_time_id IN (SELECT id FROM ip_time WHERE close_time < %s)"
    cursor.execute(select_dynamic_data_query, (two_days_ago,))
    dynamic_data_rows = cursor.fetchall()

    # Print the dynamic_data rows
    print("Dynamic Data for the previous 2 days:")
    for row in dynamic_data_rows:
        print(row)

    # Retrieve the ip_time rows for the previous 2 days
    select_ip_time_query = "SELECT * FROM ip_time WHERE close_time < %s"
    cursor.execute(select_ip_time_query, (two_days_ago,))
    ip_time_rows = cursor.fetchall()

    # Print the ip_time rows
    print("\nIP Time Data for the previous 2 days:")
    for row in ip_time_rows:
        print(row)

except Error as e:
    print("Error retrieving data from the database:", e)

finally:
    # Close the cursor and database connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
