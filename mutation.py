def mutate_string(s,i,c):
    for j in range (0,len(s)):
        if j==i:
            z=s.replace(s[j],c)
            
    return(z)
            
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
