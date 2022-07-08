
s = ""

x = ""
for i in range(len(s)):
    j, n = 0, 0
    while (i +n) != (len(s)-1) and s[i] == s[i+n+1]:
        n += 1 
        # print(n,s[i],i)
        while i-j >= 0 and i+n+1+j <= len(s):
            if s[i-j] == s[i+n+j]:
                if len(x) < 2*j +n+ 2 :
                    x = s[i-j:i+j+n+1]
                    # print(x)
                else:
                    pass
                j +=1
            else:
                break
           
    else:
        j = 0
        while i-j >= 0 and i+j < len(s):
            # print(s[i-j:i+j],s[i], s[i-j] == s[i+j])
            if s[i-j] == s[i+j]:
                # print(i, j,s[i], s[i-j:i+j+1])
                if len(x) < 2*j + 1 :
                    x = s[i-j:i+j+1]
                    # print(x)
                else:
                    pass
                j +=1
            else:
                break
    print (x) 
