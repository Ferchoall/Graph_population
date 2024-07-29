import utils 
import read_csv
import charts

def run():
  data = read_csv.read_csv('./world_population.csv')
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
 
  
  
  
  print(result)

if __name__== '__main__': # Este if es para que el archivo se pueda ejecutar como un script desde la terminal
  run()