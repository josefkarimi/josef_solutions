l = int(input())
st = input()
mylist = st.split(" ")
ans = ""
for i in range(len(mylist)-1,-1,-1):
    ans += mylist[i] +" "
print(ans[0:(len(ans)-1)])