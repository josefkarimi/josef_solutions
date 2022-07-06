from operator import index


word1 = "rosesdfghjk"
word2 = "horse"
h, k = "", ""
for i in word2:
    if i in word1:
        k += i
        print(k)

for i in word1:
    if i in word2:
        h += i
        print(h)
A = [[0 for n in (range(len(k)))] for i in range(len(k))]

for i in k:
    for j in h : 
        if i == j :
            for n in range (k.index(i), len(k)):
                for s in range (h.index(j), len(h)):
                    print(n, s)
                    A[n][s] += 1

print(A)


# for i in word2:
#     word1 = www
#     word2 = www2[www2.index(i):len(www2)]
#     for n in word2:    
#         if i in word1:
#             word1 = word1[word1.index(i):len(word1)]
#             print(word1,i,n)

# print(k, h)
# if h == k :
#     print(len(word1) + len(word2) - len(h) - len(k))
# else:
#     for i in k:
#         if i in h :

#     for k in range(len(word2)):
#         for i in range(k+1, len(word2)+1):
#             if word2[k:i] in word1:
#                 if len(word2[k:i]) > fst:
#                     fst = len(word2[k:i])
#                     print(word2[k:i])
#                 else:
#                     pass
#             else:
#                 break