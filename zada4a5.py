name = input()
stop = input("type end term to stop")
number = 0
sredno = 0
while stop != "end term":
    stop = input("type end term to stop")
    num = int(input("enter number"))
    if 2 <= num <= 6:
        number += num
    else: 
        print("invalid number")
    sredno += 1
print(number/sredno)
        