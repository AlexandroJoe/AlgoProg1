a = eval((input("Enter the subtotal : $")))
b = eval(input("Enter tip amount (as a %) :"))
tip = (b / 100) * a
total = a + tip

print("Enter the subtotal: $", "{:,.2f}".format(a))
print("Subtotal: $", "{:,.2f}".format(a))
print("Tip: $", "{:,.2f}".format(tip))
print("Total: $", "{:,.2f}".format(total))

