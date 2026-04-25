def decompress(s):
    char_list = s.split(" ")
    
    numbers = []
    #print(list_possibly_numbers)
    
    for char in char_list:
        try:
            numbers.append(int(char))
                
        except:
            continue    
    
    #print(numbers)
    
    for number in numbers:
        update = char_list[int(number)-1]
        #print(update)
        s = s.replace(str(number), update, 1)
        index = char_list.index(str(number))
        char_list[index] = update
        #print(char_list)
        
    
    
    
    return s


print(len(decompress("practice makes perfect and 3 1 2 3")))

print(len("practice makes perfect and perfect practice makes perfect"))