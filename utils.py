def data_by_sex(data, sex):
    result = list(filter(lambda item : item['Sex'] == sex, data))
    return result

def data_by_attack(data, attack):
    result = list(filter(lambda item : item['Heart_Attack'] == attack, data))
    return result

def data_by_smoke_status(data, status):
    result = list(filter(lambda item : item['Smoking_Status'] == status, data))
    return result

def data_by_diabetes(data, diabetes):
    result = list(filter(lambda item : item['Diabetes'] == diabetes, data))
    return result

def data_by_diet(data, diet):
    result = list(filter(lambda item : item['Diet_Type'] == diet, data))
    return result

def data_by_age(data, age):
    result = list(filter(lambda item : item['Age_Group'] == age, data))
    return result

def graph_data(result):
    # Obtener una lista de la columna Smoking_Status
    Smok_status = list(map(lambda x : x['Smoking_Status'], result))
    # Contar los valores repetidos de la lista Smok_Status
    Non_Smoker = Smok_status.count('Non-Smoker')
    Cur_Smoker = Smok_status.count('Current Smoker')
    Ex_Smoker = Smok_status.count('Ex-Smoker')
    # Asignar los values y labels a graficar
    values = [Non_Smoker, Cur_Smoker, Ex_Smoker]
    labels = list(set(Smok_status))
    #print(values)
    #print(labels)
    return labels, values


def aditional_filter(result, response):
    if response == 'Yes':
        options = ['Diabetes', 'Diet', 'Age']
        d_filter = input(f'Filter by? {options} ==> ')
        if d_filter == 'Smoke Status':
            status = input('Smoking Status (Non-Smoker, Current Smoker, Ex-Smoker) ==> ')
            result = data_by_smoke_status(result, status)
        elif d_filter == 'Diabetes':
            diabetes = input('Diabetes? (Yes, No) ==> ')
            result = data_by_diabetes(result, diabetes)
        elif d_filter == 'Diet':
            diet = input('Enter diet type (Healthy, Mixed, Unhealthy) ==> ')
            result = data_by_diet(result, diet)
        elif d_filter == 'Age':
            age = input('Enter age group (Adult, Youth) ==> ')
            result = data_by_age(result, age)
        #print(result_2)
        #print(len(result_2))
    else:
        result = result
    return result
