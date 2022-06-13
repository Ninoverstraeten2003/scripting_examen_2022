# Write your solution in this file
from itertools import chain 
with open('words.txt','r') as words:
    with open('output.txt', 'w') as output:
        words_set = set()
        for word in words:
            words_set.add(word.strip())
        words_set = list(words_set)
    
    
        secret_word = str('01234567')
        dictt = {
            'a':chain(range(1,2),range(2,8)),
            'b':chain(range(0,1),range(2,8)),
            'c':chain(range(0,2),range(3,8)),
            'd':chain(range(0,3),range(4,8)),
            'x':chain(range(0,5),range(6,8))
        }
        
        no = ['e','f','g','h']
        words = []
        for word in words_set:
            status = True
            for letter in word:
                if letter in no:
                    status = False
                    continue
            if status: 
                words.append(word)
        
        words2 = []
        for word in words:
            status = True
            for index, letter in tuple(enumerate(word)):
                if letter in ['a','b','c','d','x']:
                    if index not in dictt[letter]:
                        status = False 
                        continue
            if status:
                words2.append(word)
        
        for w in words2:
            status = True
            for i in ['a','b','c','d','e','x']:
               
                if w.count(i) != 1:
                    status = False
                    continue
            if status:
                output.write(f"{w}\n")
                    
                    
                
            
            
            
                    
                    
            
            
    
    
        
        