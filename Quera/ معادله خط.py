s = input()
s = s.split(" ")
# print(s)
a = int(s[0])
b = int(s[1])

# if a == b == 0:
#     print("infinite")
# elif a == 0:
#     print("invalid")
# else:
#     print("unique")

if a != 0:
    print("unique")
elif b == 0:
    print("infinite")
else:
    print("invalid")
