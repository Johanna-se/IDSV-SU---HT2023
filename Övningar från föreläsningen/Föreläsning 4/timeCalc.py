hour = int(input("Timme: "))
minutes = int(input("Minuter: "))
after_mid = hour * 60 + minutes

to_add = int(input("Minuter att addera: "))

after_mid += to_add

print("Sluttimme:", after_mid // 60 % 24)
print("Slutminuter:", after_mid % 60)
