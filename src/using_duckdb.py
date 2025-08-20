import duckdb as db
import time


#Cria a consulta na base utilizando o DuckDB
def duckdb_consulta():
    db.sql(""" SELECT station,
        MIN(temperature) as temp_min,
        CAST(AVG(temperature) AS DECIMAL(3,1)) AS temp_media,
        MAX(temperature) as temp_max
        from read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station;""").show()


if __name__ == "__main__":
    import time
    inicio = time.time()
    duckdb_consulta()
    fim = time.time()
    print(f'Processamento concluido em {fim - inicio:.2f} segundos') 