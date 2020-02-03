def add():
  lst = []
  rand = range(int(input("Number of students available")))
  lst = ['Student ' +str(x) for x in rand]
  return lst

print(add())