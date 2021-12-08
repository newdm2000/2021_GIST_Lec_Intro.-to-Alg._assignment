def LanguageOrder(words):
    dag = [[None for col in range(26)] for row in range(26)]
    wlist = []
    ret = []
    for i in range(len(words)-1):
        k = 0
        while( k < len(words[i]) and k < len(words[i+1])):
            if words[i][k] != words[i+1][k]:
                dag[ord(words[i][k]) - ord("a")][ord(words[i+1][k]) - ord("a")] = 1
                #dag[ord(words[i+1][k]) - ord("a")][ord(words[i][k]) - ord("a")] = 0
                
                st = False
                for l in range(len(wlist)):
                    if wlist[l] == words[i][k]:
                        st = True
                    else:
                        pass
                if st == False:
                    wlist.append(words[i][k])
                    
                st = False
                for l in range(len(wlist)):
                    if wlist[l] == words[i+1][k]:
                        st = True
                    else:
                        pass
                if st == False:
                    wlist.append(words[i+1][k])    
                
                break    
            
            else:
                k += 1
                     
    k=0
    while(wlist):
        stt = True
        if k >= len(wlist):
            return ""
        
        for i2 in range(len(wlist)):
            kk = wlist[i2]
            if dag[ord(kk)-ord('a')][ord(wlist[k]) - ord('a')] == 1:
                stt=False
                break
            else:
                pass
            
        if stt == True:
            for i3 in range(len(wlist)):
                kk = wlist[i3]
                dag[ord(wlist[k])-ord('a')][ord(kk) - ord('a')] = 0
            ret.append(wlist[k])
            wlist.pop(k)
            k=0
        else:
            k = k + 1     
    return "".join(ret)
