import random

lessons = [
    {
        "numLess": 1,
        "name": "Home Row",
        "explanation": "Posiciona tus dedos sobre la fila central del teclado",
        "category": "a-ñ",
    },
    {
        "numLess": 2,
        "name": "Top Row",
        "explanation": "Posiciona tus dedos sobre la fila superior del teclado",
        "category": "q-p"
    },
    {
        "numLess": 3,
        "name": "Bottom Row",
        "explanation": "Posiciona tus dedos sobre la fila inferior del teclado",
        "category":  """z-""-"""
    },
    {
        "numLess": 4,
        "name": "Numeric Row",
        "explanation": "Posiciona tus dedos sobre la fila numérica del teclado",
        "category": "1-0"
    },
]

randomText = [
    {
        "id": 1,
        "contents": "Aunque la gente feliz digan que lo son, nadie esta satisfecho: siempre tenemos que estar con la mujer mas hermosa, con la casa mas grande, cambiando coches, deseando lo que no tenemos."
    },
    {
        "id": 2,
        "contents": 'Creo que la iluminacion o revelacion vienen en la v"id"a diaria. Busco el disfrute, la paz de la accion. Necesitas actuar. Hubiera parado de escribir hace años si fuese por el dinero'
    },
    {
        "id": 3,
        "contents": "La cosa mas importante en todas las relaciones humanas es la conversacion, pero la gente ya no habla, no se sientan y escuchan. Van al cine, al teatro, ven la television, escuchan la radio, leen libros, pero casi no hablan. Si queremos cambiar el mundo, tenemos que volver al tiempo en que los guerreros se sentaban alrededor de un fuego a contar historias"
    },
    {
        "id": 4,
        "contents": "Un niño puede enseñar a un adulto tres cosas: ser feliz sin razon, siempre estar ocupado con algo y saber como demandar con toda su voluntad lo que desea"
    },
    {
        "id": 5,
        "contents": "No permitas que tu mente le diga a tu corazon que debe hacer"
    }
]

ranking = [
    {
        "username": "ElOaks",
        "wpm": 72
    },
    {
        "username": "AngelogroPistaches",
        "wpm": 73
    },
    {
        "username": "ElGrobas",
        "wpm": 69
    },
    {
        "username": "Mañuel",
        "wpm": 70
    },
    {
        "username": "SilisiosElDelFarnais",
        "wpm": 66
    },
    {
        "username": "DieguitoMaradona",
        "wpm": 75
    },
]

def getLessons(numLess=None):
    dataList = []
    if numLess:
        if numLess > len(lessons):
            return []
        return lessons[numLess-1]
    return lessons

def getContent(numLess=None):
    if numLess:
        if numLess >= len(randomText):
            return []
        return randomText[numLess-1]["contents"]
    
    textos = []
    for text in randomText:
        textos.append(text["contents"])
    
    return textos

def getActualRanking():
    ranking_ordenado = sorted(ranking, key=lambda x: x["wpm"], reverse=True)
    return ranking_ordenado


def updateRanking(user, wpm):
    return True


def getRandomText():
    ramdom_lesson = random.randint(0, len(randomText))
    
    random_text = {
        'content': randomText[ramdom_lesson-1]["contents"]
    }

    return [random_text]
