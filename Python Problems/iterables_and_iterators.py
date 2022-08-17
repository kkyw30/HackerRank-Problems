import itertools

if __name__ == '__main__':
    N = int(input())
    input_letters = input() 
    K = int(input())
    
    letters = [] 
    for letter in input_letters:
        if letter != ' ':
            letters.append(letter)
            
    # built-in itertools method to find all sublists of certain length K
    all_subs = list(itertools.combinations(letters, K))
    
    has_a = 0
    for sub in all_subs:
        if 'a' in sub:
            has_a += 1
            
    print(has_a / len(all_subs))
    