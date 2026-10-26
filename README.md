# Tarea 3 - Procesamiento de Datos con Apache Spark (Modo Batch)

## 📌 Información General
* **Curso:** Big Data  
* **Institución:** Universidad Nacional Abierta y a Distancia (UNAD)  
* **Estudiante:** Jorge Armando Acosta Vásquez  
* **Tutor:** Javier Antonio Ballesteros Ricaurte  
* **Fecha:** Octubre de 2026  

---

## 🚀 Descripción del Proyecto
Este repositorio contiene el desarrollo práctico para el procesamiento por lotes (*batch*) de un conjunto de datos masivo utilizando **PySpark** sobre un entorno de almacenamiento distribuido en **Hadoop (HDFS)**.

### Dataset Utilizado
* **Nombre:** Resultados de los sorteos de loterías  
* **Fuente:** Portal Oficial de Datos Abiertos de Colombia (`datos.gov.co`)  
* **Ubicación en Clúster:** `hdfs://localhost:9000/Tarea3/dataset_nuevo.csv`  

---

## ⚙️ Estructura y Lógica del Código (`procesamiento_batch_loterias.py`)

El script en Python realiza el siguiente flujo de procesamiento:

1. **Inicialización de la Sesión de Spark:** Configura la aplicación con nombre `Tarea3-Batch-ProcesamientoLoterias` y ajusta el nivel de registros (*log level*) a `WARN` para una consola limpia.
2. **Lectura In-Memory desde HDFS:** Carga el archivo CSV desde la ruta distribuida infiriendo automáticamente el esquema y reconociendo encabezados.
3. **Exploración Inicial (EDA) y Limpieza:** Imprime la estructura de columnas (`printSchema`), elimina registros nulos (`dropna`) y muestra una muestra representativa de variables principales (*año, mes, fecha, lotería y tipo de premio*).
4. **Agregación Analítica:** Agrupa los registros por la columna `loter_a`, calcula el conteo total de sorteos por entidad y ordena los resultados de forma descendente.
5. **Monitoreo en Spark UI:** Incorpora una pausa activa mediante `time.sleep(300)` que mantiene viva la sesión durante 5 minutos para permitir la inspección de *Jobs*, *Stages* y ejecuciones en la interfaz web (`http://localhost:4040`).

---

## 🛠️ Requisitos del Entorno
* Java JDK 8 o 11  
* Apache Hadoop (HDFS activo en puerto 9000)  
* Apache Spark (PySpark)  
* Python 3.x  

---

## ✒️ Ejecución del Script
Para ejecutar este script en el entorno de comandos (PuTTY / Terminal Linux):

```bash
spark-submit procesamiento_batch_loterias.py
