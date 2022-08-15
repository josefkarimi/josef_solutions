stones = [2,7,4,1,8,1]
while len(stones) > 1:
    y = stones.pop(stones.index(max(stones)))
    x = stones.pop(stones.index(max(stones)))
    
    if x == y:
        continue
    else:
        stones.append(y-x)
    print("stones", stones)
stones = []
print(stones[0])