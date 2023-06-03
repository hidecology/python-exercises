m = 1
# m = 2
# m = 4

if m == 2:
    print(28)
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print(31)
elif m == 4 or m == 6 or m == 9 or m == 11:
    print(30)

# 他のアプローチ
# if 0 < m and m <= 12:
#     if m == 2:
#         print(28)
#     else:
#         baseM = (m - 1) % 7
#         if baseM % 2 == 0:
#             print(31)
#         else:
#             print(30)