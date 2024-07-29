import utils 
import read_csv
import charts

def run():
    data = read_csv.read_csv('./world_population.csv')
    continent = input('Type continent => ')
    
    data = list(filter(lambda item: item['Continent'] == continent,data))
    
    countries = list(map(lambda x:x['Country/Territory'], data))
    percentages = list(map(lambda x:x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    



if __name__== '__main__': # Este if es para que el archivo se pueda ejecutar como un script desde la terminal
  run()