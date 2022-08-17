# order is lowercase, uppercase, odd digits, even digits 
if __name__ == '__main__':
    input_string = input() 
    
    letters = [] 
    digits = [] 
    
    for i in range(0, len(input_string)):
        if ord(input_string[i]) >= 48 and ord(input_string[i]) <= 57:
            digits.append(input_string[i])
        else:
            letters.append(input_string[i])
            
    lowercase = [] 
    uppercase = [] 
    for emnt in letters:
        if ord(emnt) >= 97 and ord(emnt) <= 122:
            lowercase.append(emnt)
        else:
            uppercase.append(emnt)
            
    odd = [] 
    even = [] 
    for emnt in digits:
        if (int(emnt) % 2 == 1):
            odd.append(emnt)
        else:
            even.append(emnt)
            
    lowercase.sort() 
    uppercase.sort() 
    odd.sort() 
    even.sort() 
    
    output = '' 
    for x in lowercase:
        output += x 
        
    for x in uppercase:
        output += x 
        
    for x in odd:
        output += x
        
    for x in even:
        output += x 
        
    print(output)