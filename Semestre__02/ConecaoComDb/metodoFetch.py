import oracledb

conn = oracledb . connect ( user ='rm551472', password ='041093', dsn ="oracle.fiap.com.br/orcl")
print (" Database version :", conn.version )

cur = conn.cursor () # Criar um cursor


rows = cur.fetchall () # Recuperar os resultados da consulta
for reg in rows:
    print(reg)
    
# while True:
#     regs = cur.fetchmany()
#     if not regs:
#         break
#     for reg in regs:
#         print(reg)

cur.close() # Fechar o cursor
conn.close() # Fechar a conex~ao

