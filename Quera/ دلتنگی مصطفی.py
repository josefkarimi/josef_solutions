def newnumber(x):
    new = int(x)
    
    for k in range(len(x)):
        # print(new,x[k])
        new += int(x[k])
    return new


nums = []
for _ in range(int(input())):
    nums.append(int(input()))

new_nums = set()
for i in range(max(nums)):
    new_nums.add(newnumber(str(i)))

for n in range(len(nums)):
    if nums[n] in new_nums:
        print("Yes")
    else:
        print("No")