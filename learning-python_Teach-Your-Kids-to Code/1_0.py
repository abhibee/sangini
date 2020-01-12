def toffeecounting(students, toffees):
    return students * toffees


students = float(input('Enter the number of students in your school :'))
toffees = float(
    input('Enter the number of tofees you want to give each of them :'))
print("The total number of tofees you need to buy are :",
      toffeecounting(students, toffees))
