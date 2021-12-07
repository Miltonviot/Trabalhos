-- ROLLBACK explicitas

BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;


COPY trb1(title,score,id,url,comms_num,created,body,timestamp)
FROM '/home/milton/Documentos/planilha_ok.csv'
DELIMITER ';' 
CSV HEADER;
rollback
end TRANSACTION;
