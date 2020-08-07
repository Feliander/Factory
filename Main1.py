import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="admin",
  database="mydb"
)
mycursor = mydb.cursor()
sql = 'CREATE TABLE worktime (' \
      'id INT AUTO_INCREMENT PRIMARY KEY,' \
      'name VARCHAR(20),' \
      'action VARCHAR (20),' \
      'totaltime INT,' \
      'plantime INT,' \
      'setup INT,' \
      'autoserv INT,' \
      'ppr INT,' \
      'break INT,' \
      'material INT,' \
      'task INT,' \
      'maket INT,' \
      'secs INT,' \
      'minutes INT,' \
      'hours INT,' \
      'day INT,' \
      'month INT,' \
      'year INT' \
      ')'
mycursor.execute(sql)


