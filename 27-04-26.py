#Given a word, return its score using a standard letter-value table:
#
#Letter	Value
#A	1
#B	2
#...	...
#Z	26
#Upper and lowercase letters have the same value.

def get_word_score(word):
    values_table = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26
    }
    
    total_count = 0
    
    for char in word:
        char_minus = char.lower()
        total_count += values_table[char_minus]
        
    return total_count

print(get_word_score("hippopotamus"))