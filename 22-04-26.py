# Hoy es el Día de la Tierra. A partir de una lista de objetos que hayas recogido, calcula tu puntuación total de limpieza según las reglas que se indican a continuación.
# 
# Los artículos que se entregarán serán uno de los siguientes:
# 
# Artículo	Valor base
# "bottle"	10
# "can"	6
# "bag"	8
# "tire"	35
# "straw"	4
# "cardboard"	3
# "newspaper"	3
# "shoe"	12
# "electronics"	25
# "battery"	18
# "mattress"	38
# Un objeto raro se representa como ["rare", value]. Por ejemplo, ["rare", 80]. Los objetos raros no reciben bonificación por racha.
# 
# Bonificación por racha: Si el mismo artículo aparece consecutivamente, obtiene puntos de bonificación crecientes.
# 
# Primera aparición consecutiva: valor base
# Segundo: valor base + 1
# Tercero: valor base + 2
# etc.
# Multiplicador del quinto artículo: Cada quinto artículo recolectado recibe un multiplicador.
# 
# Quinto elemento: *2
# Décimo elemento: *3
# etc.
# Aplica el multiplicador después de calcular las bonificaciones.


def get_cleanup_score(items):
    points = {
        "bottle": 10,
        "can":6,
        "bag" : 8,
        "tire"	:35,
        "straw"	:4,
        "cardboard":	3,
        "newspaper"	:3,
        "shoe"	:12,
        "electronics"	:25,
        "battery":	18,
        "mattress"	:38
    }
     
    score = 0 # Score final
    streak = 0 # Racha de consecutivos
    cincuesimas = 0 # Para saber cuantas rachas de 5 van
    prev_item = None # Item anterior
    for index, item in enumerate(items):
        puntuacion = 0
        if type(item) == list:
            puntuacion = item[1]
            streak = 0
            prev_item = None
        
        elif streak > 0 and prev_item == item:
            puntuacion = points[item] + streak
            streak += 1
            
        else:
            puntuacion = points[item]
            streak = 1
            prev_item = item
         
        if index+1 in range(0, len(items)+1, 5):
            puntuacion *= (2 + cincuesimas)
            cincuesimas += 1

        score += puntuacion
        print(score)
    return score

print(get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]))