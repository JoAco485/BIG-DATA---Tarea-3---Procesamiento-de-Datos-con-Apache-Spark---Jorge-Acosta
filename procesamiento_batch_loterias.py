from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count
import time

# 1. Inicializar la sesión de Spark
spark = SparkSession.builder \
    .appName("Tarea3-Batch-ProcesamientoLoterias") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 2. Cargar el dataset desde HDFS
ruta_hdfs = "hdfs://localhost:9000/Tarea3/dataset_nuevo.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(ruta_hdfs)

print("=== 1. ESQUEMA DEL CONJUNTO DE DATOS ===")
df.printSchema()

# 3. Limpieza básica
df_limpio = df.dropna()
print(f"Total de registros limpios: {df_limpio.count()}")

print("\n=== 2. MUESTRA DE DATOS PRINCIPALES ===")
df_limpio.select(
    "a_o_del_sorteo", 
    "mes_del_sorteo", 
    "fecha_del_sorteo", 
    "loter_a", 
    "tipo_de_premio"
).show(10, truncate=False)

print("\n=== 3. ANÁLISIS: TOTAL DE SORTEOS POR LOTERÍA ===")
df_limpio.groupBy("loter_a") \
    .agg(count("*").alias("total_sorteos")) \
    .orderBy(col("total_sorteos").desc()) \
    .show(15, truncate=False)

# 4. Pausa para permitir la visualización en la Spark UI (Puerto 4040)
print("\n" + "="*50)
print("¡Procesamiento batch finalizado con éxito!")
print("La Spark UI está disponible en: http://localhost:4040 o http://192.168.1.19:4040")
print("El script se mantendrá activo por 5 minutos para que puedas revisar las pestañas.")
print("="*50 + "\n")

time.sleep(300) # Mantiene la sesión abierta por 300 segundos (5 minutos)

spark.stop()