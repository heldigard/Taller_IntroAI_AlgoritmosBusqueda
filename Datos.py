from grafos import Estado, Accion


class Datos:
    accN = Accion('N')
    accS = Accion('S')
    accE = Accion('E')
    accO = Accion('O')
    accNE = Accion('NE')
    accNO = Accion('NO')
    accSE = Accion('SE')
    accSO = Accion('SO')

    manizales = Estado('Manizales', [accN])
    medellin = Estado('Medellin', [accS, accNO, accNE])
    santafe = Estado('Santa Fe', [accNO, accSE])
    dabeiba = Estado('Dabeiba', [accNO, accSE])
    chigorodo = Estado('Chigorodo', [accN, accSE])
    arboletes = Estado('Arboletes', [accS, accE])
    barbosa = Estado('Barbosa', [accSO, accNE, accNO])
    yarumal = Estado('Yarumal', [accSE, accNE, accE])
    cisneros = Estado('Cisneros', [accSO, accE])
    amalfi = Estado('Amalfi', [accO, accE])
    maceo = Estado('Maceo', [accO, accN])
    remedios = Estado('Remedios', [accNO, accO, accS])
    caucasia = Estado('Caucasia', [accNO, accSE, accSO])
    monteria = Estado('Monteria', [accO, accNE, accSE])
    planetarica = Estado('Planeta Rica', [accNO, accN, accSE])
    sahagun = Estado('Sahagun', [accSO, accS, accN])
    cienaga = Estado('Cienaga', [accO, accNE])
    cerete = Estado('Cerete', [accE, accN])
    covenias = Estado('Coveñas', [accS, accNE])
    sincelejo = Estado('Sincelejo', [accNO, accS])
    tolu = Estado('Tolu', [accSO, accSE])

    acciones = {
        'Manizales': {'N': medellin},
        'Medellin': {'S': manizales, 'NO': santafe, 'NE': barbosa},
        'Santa Fe': {'NO': dabeiba, 'SE': medellin},
        'Dabeiba': {'NO': chigorodo, 'SE': santafe},
        'Chigorodo': {'N': arboletes, 'SE': dabeiba},
        'Arboletes': {'S': chigorodo, 'E': monteria},
        'Barbosa': {'NO': yarumal, 'SO': medellin, 'NE': cisneros},
        'Yarumal': {'SE': barbosa, 'NE': caucasia, 'E': amalfi},
        'Cisneros': {'SO': barbosa, 'E': maceo},
        'Amalfi': {'O': yarumal, 'E': remedios},
        'Maceo': {'O': cisneros, 'N': remedios},
        'Remedios': {'NO': caucasia, 'O': amalfi, 'S': maceo},
        'Caucasia': {'NO': planetarica, 'SE': remedios, 'SO': yarumal},
        'Monteria': {'O': arboletes, 'NE': cerete, 'SE': planetarica},
        'Planeta Rica': {'NO': monteria, 'N': sahagun, 'SE': caucasia},
        'Sahagun': {'SO': cienaga, 'S': planetarica, 'N': sincelejo},
        'Cienaga': {'O': cerete, 'NE': sahagun},
        'Cerete': {'E': cienaga, 'N': covenias},
        'Coveñas': {'S': cerete, 'NE': tolu},
        'Sincelejo': {'NO': tolu, 'S': sahagun},
        'Tolu': {'SO': covenias, 'SE': sincelejo}
    }

    costos = {
        'Manizales': {'N': 228},
        'Medellin': {'S': 228, 'NO': 56, 'NE': 44},
        'Santa Fe': {'NO': 103, 'SE': 56},
        'Dabeiba': {'NO': 109, 'SE': 103},
        'Chigorodo': {'N': 177, 'SE': 109},
        'Arboletes': {'S': 177, 'E': 69},
        'Barbosa': {'NO': 99, 'SO': 44, 'NE': 38},
        'Yarumal': {'SE': 99, 'NE': 161, 'E': 157},
        'Cisneros': {'SO': 38, 'E': 48},
        'Amalfi': {'O': 157, 'E': 83},
        'Maceo': {'O': 48, 'N': 83},
        'Remedios': {'NO': 148, 'O': 83, 'S': 83},
        'Caucasia': {'NO': 70, 'SE': 148, 'SO': 161},
        'Monteria': {'O': 69, 'NE': 23, 'SE': 54},
        'Planeta Rica': {'NO': 54, 'N': 73, 'SE': 70},
        'Sahagun': {'SO': 34, 'S': 73, 'N': 48},
        'Cienaga': {'O': 19, 'NE': 34},
        'Cerete': {'E': 19, 'N': 73},
        'Coveñas': {'S': 73, 'NE': 22},
        'Sincelejo': {'NO': 40, 'S': 48},
        'Tolu': {'SO': 22, 'SE': 40}
    }