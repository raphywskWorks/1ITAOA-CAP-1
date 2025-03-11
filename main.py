import math
import os

def calcAreaAvailable(area, figure, streetSize, spaceBetweenStreets):
    if figure == 'retangulo':
        totalStreetSize = streetSize + spaceBetweenStreets
        streetQdt = math.floor(area / totalStreetSize)
        areaOccupiedByStreets = streetQdt * streetSize
        areaAvailable = area - areaOccupiedByStreets
        return {'plantingArea': areaAvailable, 'numberOfStreets': streetQdt}

    if figure == 'triangulo':
        base = math.sqrt(2 * area)
        height = base / 2
        totalArea = (base * height) / 2
        totalStreetSize = streetSize + spaceBetweenStreets
        streetsQtd = math.floor(height / totalStreetSize)
        areaAvailable = totalArea - (streetsQtd * streetSize * base / totalArea)
        return {'plantingArea': areaAvailable, 'numberOfStreets': streetsQtd}

# nome, produto aplicado, figura geométrica para plantio, largura da rua, espaço entre ruas
cultures = [
    ['milho', 'Fosfato Monoamônico', 'retangulo', 1, 1],
    ['laranja', 'Diclorofenoxiacético', 'triangulo', 2, 1],
]

# Quantidade necessária de produto, em ml por m2
products = {'Fosfato Monoamônico': 5, 'Diclorofenoxiacético': 0.15}

# Indice do produto, área disponível em m2.
calculatedPlantingAreas = []

welcomeMessage = '''

___________                        _________      .__          __  .__                      
\_   _____/____ _______  _____    /   _____/ ____ |  |  __ ___/  |_|__| ____   ____   ______
 |    __) \__  \\_  __ \/     \   \_____  \ /  _ \|  | |  |  \   __\  |/  _ \ /    \ /  ___/
 |     \   / __ \|  | \/  Y Y  \  /        (  <_> )  |_|  |  /|  | |  (  <_> )   |  \\___ \ 
 \___  /  (____  /__|  |__|_|  / /_______  /\____/|____/____/ |__| |__|\____/|___|  /____  >
     \/        \/            \/          \/                                       \/     \/ 

    \n
    Bem vindo a FarmTech Solutions!
    \n
    Aqui você consegue planejar o seu plantio com muito mais eficiência!
    \n
    Vamos começar?
    \n\n\n
'''


option = 0
currentCultureCalculated = 0
phases = [
    {'text': welcomeMessage},
    {'text': 'Escolha uma cultura: ', 'helper': 'Digite 1 para milho e 2 para laranja ou digite 0 para sair'},
    {'text': 'Insira a área disponível total: ', 'helper': 'Digite o valor da area em metros quadrados, ou digite 0 para sair'},
    {'text': 'Calculo finalizado!', 'helper': ''},
    {'text': 'Escolha uma nova opção: ', 'helper': 'Digite 1 para realizar um novo calculo, 2 para editar um calculo já realizado ou 0 para sair'}
]

def clearTerminal():
    system = os.name
    if system == 'nt':
        os.system('cls')
        return
    os.system('clear')

def addCulture(culture):
    calculatedPlantingAreas.append([culture])
    print(f'A cultura escolhida foi {cultures[culture - 1][0]}!\n')

def addTotalArea(area):
    arrayIndex = len(calculatedPlantingAreas) - 1
    arraySize = len(calculatedPlantingAreas[arrayIndex])
    if arraySize < 2:
        calculatedPlantingAreas[arrayIndex].append(area)
        return
    
    calculatedPlantingAreas[arrayIndex][1] = area

def printHelper():
    print(phases[option]['helper'])
    print('\n')

def getUserOption():
    userOption = input(phases[option]['text'])
    return userOption

def handleInvalidInput():
    clearTerminal()
    print('\nValor digitado é inválido.\n')

def showCalc():
    calculatedAreaResume = calculatedPlantingAreas[currentCultureCalculated]
    culture = cultures[calculatedAreaResume[0] - 1]
    calculated = calcAreaAvailable(calculatedAreaResume[1], culture[2], culture[3], culture[4])
    productCalculated = products[culture[1]] * calculated['plantingArea']

    userOutput = f'''A cultura escolhida foi {culture[0]}, com área total disponível para plantio de {calculatedAreaResume[1]} metros quadrados.\n
O formato da área deve ser de um {culture[2]}.\n
O total da área efetiva plantada é de {round(calculated['plantingArea'], 2)} metros quadrados, com {calculated['numberOfStreets']} ruas disponíveis para plantio.\n
A aplicação de {round(productCalculated, 2)} ml de {culture[1]} será necessária.
     '''

    print (userOutput)

while option >= 0:
    match option:
        case 0:
            clearTerminal()
            print(phases[option]['text'])
            option += 1
        case 1:
            printHelper()
            try:
                culture = int(getUserOption())
                if ( not culture ):
                    option = -1
                    break
                addCulture(culture)
                option += 1
            except Exception as e:
                handleInvalidInput()
            
        case 2:
            clearTerminal()
            printHelper()
            try:
                area = float(getUserOption())
                if ( not area ):
                    option = -1
                    break
                addTotalArea(area)    
                option += 1
            except Exception as e:
                handleInvalidInput()

        case 3:
            clearTerminal()
            showCalc()
            print(calculatedPlantingAreas)
            option += 1
        case 4:
            printHelper()
            try:
                userNewOption = int(getUserOption())
                if ( not userNewOption ):
                    option = -1
                    break

                if ( userNewOption == 1 ): 
                    currentCultureCalculated = len(calculatedPlantingAreas)
                    option = 1
                if ( userNewOption == 2 ):
                   print('editar')
                   # Criar função para editar os arrays. 
            except:
                handleInvalidInput()
