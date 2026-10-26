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
El script en Python realiza el siguiente flujo:
1. **Inicialización de la Sesión de Spark** con nivel de registros ajustado a `WARN`.
2. **Lectura desde HDFS** infiriendo el esquema y detectando los encabezados del archivo CSV.
3. **Limpieza y Exploración (EDA):** Eliminación de valores nulos y filtrado de columnas clave (*año, mes, fecha, lotería, tipo de premio*).
4. **Agregación Analítica:** Conteo total de sorteos agrupados por cada entidad de lotería de forma descendente.
5. **Monitoreo en Spark UI:** Pausa activa de 5 minutos para revisión de Jobs en el puerto `4040`.

---

## 💻 Evidencia de Ejecución y Resultados

A continuación se muestra la traza de ejecución del script directamente desde la terminal del clúster:

```text
hadoop@bigdata:~$ python3 batch_processing.py
26/10/26 23:26:19 WARN Utils: Your hostname, bigdata resolves to a loopback address: 127.0.1.1; using 192.168.1.19 instead (on interface enp0s3)
Setting default log level to "WARN".
26/10/26 23:26:20 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable

=== 1. ESQUEMA DEL CONJUNTO DE DATOS ===
root
 |-- :id: string (nullable = true)
 |-- :version: string (nullable = true)
 |-- :created_at: timestamp (nullable = true)
 |-- :updated_at: timestamp (nullable = true)
 |-- a_o_del_sorteo: integer (nullable = true)
 |-- mes_del_sorteo: integer (nullable = true)
 |-- fecha_del_sorteo: string (nullable = true)
 |-- loter_a: string (nullable = true)
 |-- n_mero_del_sorteo: integer (nullable = true)
 |-- numero_billete_ganador: integer (nullable = true)
 |-- numero_serie_ganadora: integer (nullable = true)
 |-- tipo_de_premio: string (nullable = true)

Total de registros limpios: 110037

=== 2. MUESTRA DE DATOS PRINCIPALES ===
+--------------+--------------+----------------+-------------------------+--------------+
|a_o_del_sorteo|mes_del_sorteo|fecha_del_sorteo|loter_a                  |tipo_de_premio|
+--------------+--------------+----------------+-------------------------+--------------+
|2020          |1             |31/01/2020      |Loteria del Quindio      |Mayor         |
|2020          |1             |24/01/2020      |Loteria de Bogota        |Mayor         |
|2020          |1             |29/01/2020      |Loteria de la Cruz Roja  |Mayor         |
|2020          |1             |27/01/2020      |Loteria de Medellin      |Mayor         |
|2020          |1             |13/01/2020      |Loteria de Boyaca        |Mayor         |
|2020          |1             |28/01/2020      |Loteria del Tolima       |Mayor         |
|2020          |1             |30/01/2020      |Loteria del Meta         |Mayor         |
|2020          |1             |12/01/2021      |Sorteo Extraordinario    |Mayor         |
|2020          |1             |29/01/2020      |Loteria del Huila        |Mayor         |
|2020          |1             |10/01/2020      |Loteria del Quindio      |Mayor         |
+--------------+--------------+----------------+-------------------------+--------------+
only showing top 10 rows

=== 3. ANÁLISIS: TOTAL DE SORTEOS POR LOTERÍA ===
+------------------------+-------------+
|loter_a                 |total_sorteos|
+------------------------+-------------+
|Loteria de la Cruz Roja |11443        |
|Loteria de Bogota       |9741         |
|Loteria de Boyaca       |9333         |
|Loteria de Cundinamarca |9303         |
|Loteria Santander       |8243         |
|Loteria del Meta        |8041         |
|Loteria del Huila       |7531         |
|Loteria del Valle       |7319         |
|Loteria del Quindio     |7069         |
|Loteria de Medellin     |6829         |
|Loteria del Risaralda   |6755         |
|Loteria del Cauca       |6639         |
|Loteria de Manizales    |5863         |
|Loteria del Tolima      |4343         |
|Sorteo Extra de Colombia|1475         |
+------------------------+-------------+
only showing top 15 rows

==================================================
¡Procesamiento batch finalizado con éxito!
La Spark UI está disponible en: http://localhost:4040 o [http://192.168.1.19:4040](http://192.168.1.19:4040)
El script se mantendrá activo por 5 minutos para que puedas revisar las pestañas.
==================================================
