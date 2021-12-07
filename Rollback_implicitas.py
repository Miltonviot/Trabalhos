-- ROLLBACK implicitas



import csv
import psycopg2

conn = psycopg2.connect(database="trb1", user = "postgres", password = "sapo123", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

filehandle = open('/home/milton/Documentos/reddit_vm.csv','r') 
reader = csv.reader(filehandle, delimiter=',')

for row in reader:
  
  statement = "INSERT INTO trb1(title,score,id,url,comms_num,created,body,data) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (tuple(row))
  cur.execute(statement)
  conn.rollback() 
