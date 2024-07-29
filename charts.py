import matplotlib.pyplot as plt

def generate_bar_chart(labels, values): # aca se genera la grafica
  fig, ax = plt.subplots() #son dos variables que nos da la libreria "fig" es la figura y "ax" son las cooordenadas donde se va a graficar
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values): #grafico de torta 
  fig, ax = plt.subplots() 
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.show()
  
if __name__ == '__main__':  #Aca se llama la funcion a que inice como archivo 
  labels = ['a', 'b', 'c']
  values = [100,60, 80]

 # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)