total = 0

for days in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
    sales = float(input("Total sales for\t" + days + ":"))
    total += sales
print("Total amount of sales for the week is:" + format(total, ",.2f"))
print("Average sales for the week is:" + format(total / 7, ",.2f"))
