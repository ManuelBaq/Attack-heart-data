import matplotlib.pyplot as plt

#DEFINIR GRAFICA DE BARRAS
def generate_bar_chart(labels, values): 

    fig, ax = plt.subplots()
    ax.bar(labels,values) # Especifica el tipo de grafica .bar y los ejes de la grafica (labels,values)
    plt.show()
