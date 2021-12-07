#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import psycopg2

conn = None

try:


  conn = psycopg2.connect(database="trb1", user = "postgres", password = "sapo123", host = "127.0.0.1", port = "5432")
  cur = conn.cursor()


  query = "BEGIN TRANSACTION ;COPY trb1(title,score,id,url,comms_num,created,body,data) FROM '/home/milton/Documentos/planilha_ok.csv' DELIMITER ';' CSV HEADER; end TRANSACTION ; "

  cur.execute(query)
  conn.commit()
  cur.close()

except psycopg2.DatabaseError as error:
  print(error)
finally:
  if conn is not None:
    conn.close()
