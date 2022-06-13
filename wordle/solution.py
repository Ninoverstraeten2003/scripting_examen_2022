# Write your solution in this file

with open('words.txt','r') as words:
    with open('output.txt', 'w') as output:
        words_set = set()
        for word in words:
            words_set.add(word.strip())
        words_set = list(words_set)
    
    
        secret_word = str('01234567')
        dictt = {
            'a':[1-7],
            'b':[0,2-7],
            'c':[0-1,3-7],
            'd':[0-2,4-7],
            'e':[0-3,5-7],
            'x':[4]
        }
        no = ['e','f','g','h']
        words = []
        for i in no:
            for word in words_set:
                for letter in word:
                    if i != letter:
                        words.append(word)
        for word in words:
            
            for index, letter in tuple(enumerate(word)):
                if index not in dictt(letter):
                    continue
                output.write(f"{word}\n")
            
            
            
                    
                    
            
            
    
    
        
        