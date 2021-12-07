def LanguageOrder(words):
    dag = [[None for col in range(26)] for row in range(26)]
    wlist = []
    for i in range(len(words)-1):
        k = 0
        while( k < len(words[i]) and k < len(words[i+1])):
            if words[i][k] != words[i+1][k]:
                dag[ord(words[i][k]) - ord("a")][ord(words[i+1][k]) - ord("a")] = 1
                dag[ord(words[i+1][k]) - ord("a")][ord(words[i][k]) - ord("a")] = 0
                
                j=0
                while(j<len(wlist)):
                    if wlist[j] == words[i][k]:
                        break
                    else:
                        j += 1
                    wlist.append(words[i][k])
                    
                j=0
                while(j<len(wlist)):
                    if wlist[j] == words[i+1][k]:
                        break
                    else:
                        j += 1
                    wlist.append(words[i+1][k])
                    
                break
            
            else:
                k += 1
    
    print(wlist)
        
    
words = ["xwt", "xwf", "aw", "att", "wftt"]

LanguageOrder(words)