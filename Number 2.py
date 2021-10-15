a = eval(input("Enter the plane's take off speed in m/s : "))
b = eval(input("Enter the plane;s acceleration in m/s : "))

hasil = (a**2) / (2 * b)

print("The minimum runway length needed for this airplane is ",format(hasil,'.4f'), "meters")

# input the speed
# input the acceleration
# execute the formula
# print the final value