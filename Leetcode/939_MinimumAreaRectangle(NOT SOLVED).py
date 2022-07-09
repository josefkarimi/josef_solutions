# class Solution:
#     def minAreaRect(self, points: List[List[int]]) -> int:
#         points.sort()
#         surf = 0
#         for i in range(len(points)):
#             for j in range(len(points)):
#                 for k in range(len(points)):
#                     for n in range(len(points)):
#                         if points[i][0] == points[k][0] and points[j][0] == points[n][0] and points[i][1] == points[j][1] and points[k][1] == points[n][1] : 
#                             surf = (points[j][0] - points[i][0]) * (points[n][1] - points[j][1])
#                             if surf > 0:
#                                 break
#                     if surf > 0:
#                         break
#                 if surf > 0:
#                     break
#             if surf > 0:
#                 break


#         for i in range(len(points)):
#             for j in range(len(points)):
#                 for k in range(len(points)):
#                     for n in range(len(points)):
#                         if points[i][0] == points[k][0] and points[j][0] == points[n][0] and points[i][1] == points[j][1] and points[k][1] == points[n][1] : 
#                             s = (points[j][0] - points[i][0]) * (points[n][1] - points[j][1])
#                             # print("s is ", s)
#                             # print(points[i], points[j], points[k], points[n])
#                             if s > 0 and s < surf:
#                                 surf = s
#                                 # print("surf is ", surf)

#         return (surf)




# points.sort()
# surf = []
# x = 0
# for i in range(len(points)):
#     for j in range(len(points)):
#         for k in range(len(points)):
#             for n in range(len(points)):
#                 x += 1
#                 if points[i][0] == points[k][0] and points[j][0] == points[n][0] and points[i][1] == points[j][1] and points[k][1] == points[n][1] : 
#                     if (points[j][0] - points[i][0]) * (points[n][1] - points[j][1]) > 0:
#                         surf.append((points[j][0] - points[i][0]) * (points[n][1] - points[j][1]))
# MySet = {0}
# for o in surf:
#     MySet.add(o)

# surf.sort()
# print(len(surf), len(MySet), surf[0], x, len(points))



# for i in range(len(points)):
#     for j in range(len(points)):
#         for k in range(len(points)):
#             for n in range(len(points)):
#                 if points[i][0] == points[k][0] and points[j][0] == points[n][0] and points[i][1] == points[j][1] and points[k][1] == points[n][1] : 
#                     s = (points[j][0] - points[i][0]) * (points[n][1] - points[j][1])
#                     # print("s is ", s)
#                     # print(points[i], points[j], points[k], points[n])
#                     if s > 0 and s < surf:
#                         surf = s
#                         # print("surf is ", surf)

# return (surf)




# # Function which returns subset or r length from n
# from itertools import combinations
# arr = [[1,0], [0,1], [2,3], [4,5], [3,4]]
# def rSubset(arr, r):

# 	# return list of all subsets of length r
# 	# to deal with duplicate subsets use
# 	# set(list(combinations(arr, r)))
# 	return list(combinations(arr, r))
# print(len(list(combinations(arr, 2))))

# # Driver Function
# if __name__ == "__main__":
# 	arr = [1, 2, 3, 4]
# 	r = 2
# 	print (rSubset(arr, r))





# from itertools import combinations



# points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# points = [[3801,24477],[34959,20822],[3801,18276],[34959,22107],[886,20684],[3801,20684],[13575,18276],[36134,22107],[3801,32052],[36134,20822],[25737,18276],[4056,20822],[4056,38720],[12218,20684],[1478,18276],[25737,22107],[13575,38720],[12218,38720],[11723,38720],[11723,20822],[11723,24477],[13575,20684],[3801,38720],[11723,22107],[886,24477],[39813,22107],[36134,20684],[36134,10798],[3801,20822],[12218,34924],[25737,21393],[34959,34924],[36134,18276],[11723,18276],[11723,10798],[36134,24477],[4056,24477],[4056,21393],[39813,20822],[12218,24477],[1478,20822],[25737,20822],[1478,38720],[39813,10798],[886,18276],[11723,20684],[12218,18276],[12218,21393],[1478,34924],[34959,18276],[1478,20684],[1478,21393],[886,22107],[25737,34924],[34959,21393],[34959,20684],[886,32052],[25737,10798],[12218,32052],[25737,32052],[886,34924],[39813,20684],[4056,18276],[3801,10798],[39813,24477],[39813,38720],[1478,22107],[11723,34924],[4056,32052]]
# points = [[16793,24298],[24122,35227],[32714,24298],[29233,4158],[862,7785],[31782,17366],[9191,29976],[24122,21801],[31782,4158],[32714,37583],[32714,29976],[31782,19170],[39814,29976],[862,4158],[34816,7785],[17327,29976],[16793,7785],[32714,21801],[32714,24895],[29233,19170],[17327,17366],[2226,4158],[9191,35227],[16793,4158],[31782,24298],[31782,24895],[34816,19170],[24122,24895],[862,24298],[862,24895],[2226,7785],[17327,21801],[862,17366],[34816,4158],[31782,21801],[862,19170],[2226,21801],[17327,35227],[29233,24298],[39814,24895],[862,21801],[39814,24298],[2226,35227],[39814,7785],[24122,7785],[2226,24895],[29233,29976],[9191,24895],[34816,24895],[34816,21801],[24122,19170],[32714,7785],[2226,24298],[29233,24895],[2226,17366],[34816,37583],[16793,24895],[17327,4158],[16793,37583],[24122,4158],[9191,24298],[39814,17366],[39814,35227],[29233,35227],[39814,37583],[862,29976],[29233,37583]]
# points = [[15088,28838],[34731,3459],[39142,3459],[39341,3324],[32262,34050],[37539,3324],[34731,28687],[39142,28687],[39142,644],[4845,36217],[34731,34050],[4845,28687],[37539,2844],[21270,2844],[11219,644],[32262,644],[25511,28687],[37539,2646],[37539,2580],[10074,2844],[2129,2580],[39341,28838],[2129,2646],[37539,3623],[2129,2844],[15447,4444],[4845,644],[15447,34050],[39142,36217],[15447,39373],[34731,28838],[11219,2844],[2129,3324],[39142,28838],[11219,34050],[21270,3324],[29722,39373],[37539,39373],[11219,2580],[25511,38799],[4845,2646],[39142,3623],[4845,39373],[2129,3623],[32262,3324],[4845,38799],[32262,4444],[25511,3324],[25511,2646],[25511,2580],[2129,28838],[39341,3459],[21270,28687],[25511,3623],[10074,34050],[29722,644],[25511,2844],[21270,644],[39341,28687],[10074,3459],[2129,36217],[15088,36217],[29722,2844],[34731,2646],[25511,36217],[15088,38799],[32262,3623],[15088,39373],[15088,3623],[37539,38799],[4845,34050],[39341,644],[15088,4444],[39341,4444],[10074,28838],[25511,34050],[11219,4444],[21270,39373],[25511,39373],[15088,3324],[39142,2646],[10074,39373],[25511,3459],[2129,28687],[34731,3623],[32262,28838],[39341,36217],[39341,38799],[15088,34050],[2129,34050],[4845,3623],[15447,28687],[2129,38799],[15447,3324],[15447,2646],[29722,34050],[15447,2580],[39142,39373],[25511,4444],[2129,644],[34731,39373],[37539,28687],[21270,34050],[2129,4444],[15447,2844],[29722,3459],[39341,2844],[32262,39373],[37539,3459],[39142,3324],[34731,3324],[39142,2580],[39341,2580],[15447,36217],[37539,34050],[39341,34050],[39341,39373],[10074,2646],[34731,4444],[10074,36217],[15088,2844],[4845,4444],[15447,3623]]

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        from itertools import combinations
        ind = combinations(range(len(points)), 4)
        points.sort()
        surf = 0

        while True:
            try:
                # print(ind.__next__())
                noghat = ind.__next__()
                spoint = [points[noghat[0]], points[noghat[1]], points[noghat[2]], points[noghat[3]]]
                # print(spoint)
                if spoint[0][0] == spoint[1][0] and spoint[2][0] == spoint[3][0] and spoint[0][1] == spoint[2][1] and spoint[1][1] == spoint[3][1]:
                    # print(spoint)
                    s = (spoint[1][1] - spoint[0][1]) * (spoint[3][0] - spoint[1][0])
                    # print(s)
                    if s > 0:
                        surf = s
                        print(s)
                        break
            except :
                # print("End")
                break

        while True:
            try:
                # print(ind.__next__())
                noghat = ind.__next__()
                spoint = [points[noghat[0]], points[noghat[1]], points[noghat[2]], points[noghat[3]]]
                # print(spoint)
                if spoint[0][0] == spoint[1][0] and spoint[2][0] == spoint[3][0] and spoint[0][1] == spoint[2][1] and spoint[1][1] == spoint[3][1]:
                    # print(spoint)
                    s = (spoint[1][1] - spoint[0][1]) * (spoint[3][0] - spoint[1][0])
                    # print(s)
                    if s < surf:
                        surf = s      
            except :
                # print("End")
                break

        return surf
# from itertools import combinations
# ind = combinations(range(len(points)), 4)
# points.sort()
# surf = 0

# while True:
#     try:
#         # print(ind.__next__())
#         noghat = ind.__next__()
#         spoint = [points[noghat[0]], points[noghat[1]], points[noghat[2]], points[noghat[3]]]
#         # print(spoint)
#         if spoint[0][0] == spoint[1][0] and spoint[2][0] == spoint[3][0] and spoint[0][1] == spoint[2][1] and spoint[1][1] == spoint[3][1]:
#             # print(spoint)
#             s = (spoint[1][1] - spoint[0][1]) * (spoint[3][0] - spoint[1][0])
#             print(s)
#             if s > 0:
#                 surf = s
#                 print(s)
#                 break
#     except :
#         print("End")
#         break

# while True:
#     try:
#         # print(ind.__next__())
#         noghat = ind.__next__()
#         spoint = [points[noghat[0]], points[noghat[1]], points[noghat[2]], points[noghat[3]]]
#         # print(spoint)
#         if spoint[0][0] == spoint[1][0] and spoint[2][0] == spoint[3][0] and spoint[0][1] == spoint[2][1] and spoint[1][1] == spoint[3][1]:
#             # print(spoint)
#             s = (spoint[1][1] - spoint[0][1]) * (spoint[3][0] - spoint[1][0])
#             # print(s)
#             if s < surf:
#                 surf = s      
#     except :
#         print("End")
#         break

# print( surf)