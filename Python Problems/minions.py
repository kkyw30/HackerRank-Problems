# goal to determine whether Kevin or Stuart can come up with more substrings given an inputted string (Kevin's substrings start with vowels, Stuart's substrings start with consonants)

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # for each given character in string, the number of substrings following that character 
    # is len(str) - index 
    
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if s[i] in 'AEIOU':
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart < kevin: 
        print('Kevin', kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)