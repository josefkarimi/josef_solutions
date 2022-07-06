# image = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = sc = 1
    color = 2

# image = [[0,0,0],[0,0,0]]
# sr = sc = 0
# color = 0
white = image[sr][sc]
dots = [(sr, sc)]

def coloring(a):
    if a == white:
        return color
    else:
        return a

def nextto (fx, arr, i):
    for n,m in ((i[0]-1,i[1]),(i[0],i[1]-1),(i[0],i[1]),(i[0],i[1]+1),(i[0]+1,i[1])):
        if n >=0 and m >=0:
            try :
                if arr[n][m] == white:
                    dots.append((n,m))
                arr[n][m] = fx(arr[n][m])

                # print(dots)

            except IndexError:
                pass
    dots.remove(i)
if white != color:
    # return image
    while dots:
        nextto(coloring,image,dots[0])
# return image
print(image)