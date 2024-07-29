# Graph_population

## Descripción 

Este repositorio contiene scripts en Python diseñados para analizar y visualizar datos de la población mundial. Los scripts leen datos de un archivo CSV, procesan la información según las entradas proporcionadas por el usuario y generan gráficos para visualizar los resultados.

## Estructura del Proyecto

### main.py
- Solicita al usuario ingresar el nombre de un país.
- Lee los datos de población desde `world_population.csv`.
- Filtra los datos para obtener la información del país especificado.
- Genera un gráfico de barras que muestra la población del país a lo largo de los años.

### graph_world_population.py
- Solicita al usuario ingresar el nombre de un continente.
- Lee los datos de población desde `world_population.csv`.
- Filtra los datos para obtener los países del continente especificado.
- Genera un gráfico de pastel que muestra el porcentaje de población de cada país en el continente.

## Dependencias

Para instalar las bibliotecas necesarias, ejecuta el siguiente comando:

```bash
pip install pandas matplotlib
```

## Cómo Ejecutar

1. Clona el repositorio en tu máquina local.

2. Asegúrate de que el archivo `world_population.csv` esté en el mismo directorio que los scripts.

3. Ejecuta los scripts usando Python 3.x:

   - Para ejecutar `main.py`:
     ```bash
     python main.py
     ```

   - Para ejecutar `graph_world_population.py`:
     ```bash
     python graph_world_population.py
     ```