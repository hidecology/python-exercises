def nabeatsu(n):
    if n % 3 == 0 or ("3" in str(n)):
        return "(｡Дﾟ) {0}ッ".format(n)
    else:
        return str(n)

n = 40
for i in range(1, n+1):
    print(nabeatsu(i))
print("オモローー！")