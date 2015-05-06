
import psycopg2

# Connect to an existing database


conn = psycopg2.connect(host='localhost', 
	database="examdb", user="dbo", password="pass")
