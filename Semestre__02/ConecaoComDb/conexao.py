import oracledb

conn = oracledb . connect ( user ='rm551472', password ='041093', dsn ="oracle.fiap.com.br/orcl")
print (" Database version :", conn.version )

cur = conn.cursor () # Criar um cursor

cur.execute('SELECT * FROM country') # Executar uma consulta

rows = cur.fetchall () # Recuperar os resultados da consulta
for reg in rows:
    print(reg)


cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('02','Argentina')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('03','Guatemala')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('04','Chile')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('05','Gabão')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('06','Peru')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('07','Venezuela')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('08','Congo')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('09','Africa do Sul')") # Executar uma consulta
cur.execute("INSERT INTO COUNTRY (ID,NOME) VALUES ('10','Israel')") # Executar uma consulta
conn.commit(); 

cur.execute('SELECT * FROM country') # Executar uma consulta

rows = cur.fetchall () # Recuperar os resultados da consulta
for reg in rows:
    print(reg)

cur.close() # Fechar o cursor
conn.close() # Fechar a conex~ao

