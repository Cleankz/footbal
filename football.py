def Football(F,N):
    reverse = sorted(F)
    dif = []
    for i in range(N):
        if F[i] != reverse[i]:
            dif.append(F[i])
    if len(dif) == 2:
        return True
    else:
        dif.sort()
        s1 = str(dif)
        s2 = str(reverse)
        s1 = s1.replace("[",'')
        s1 = s1.replace("]",'')
        s2 = s2.replace("[",'')
        s2 = s2.replace("]",'')
        if s1 in s2:
            return True
        else:
            return False