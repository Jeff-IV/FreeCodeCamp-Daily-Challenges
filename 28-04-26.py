def get_number_words(n: int) -> str:
    ones = [
        "zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ] 
    
    tens = [
        None, None, "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    if 0 <= n < 20:
        return ones[n]
    elif n % 10 == 0:
        return tens[n // 10] # n // 10 para que nos de un indice válido
    else:
        return tens[n // 10] + "-" + ones[n % 10] # n % 10 nos regala el residuo de la division entre n y 10
    
print(get_number_words(88))