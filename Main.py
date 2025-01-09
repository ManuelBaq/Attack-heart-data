import read_csv
import utils
import charts

def run():
    data = read_csv.read_csv('heart_attack.csv')
    # Seleccionar el tipo de género que quiere filtrarse
    sex = input('Gender (Male, Female, Other) ==> ')
    # Filtrar según el género
    result = utils.data_by_sex(data, sex)
    # Filtrar por ataque al corazón
    attack = input('Heart attack status (Yes,No) ==> ')
    result = utils.data_by_attack(result, attack)
    # Preguntar por un filtro adicional
    response = input('Would you like another filter? (Yes,No) ==> ')
    # Aplicar filtro adicional
    result = utils.aditional_filter(result, response)
    # Nuevo filtro?
    response = input('Would you like another filter? (Yes,No) ==> ')
    result = utils.aditional_filter(result, response)
    #print(result)
    #print(len(result))
    # Realizar una grafica de barras teniendo en cuenta los filtros anteriores para ver la relación
    # con su estado actual de fumadores
    labels, values = utils.graph_data(result)
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()
