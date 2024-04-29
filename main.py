def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operator={
  "+":add,
  "-":subtract,
  "/":divide,
  "*":multiply
}
def calculater():
  n1=float(input("what is the first number? "))
  
  keep_going=True
  while keep_going==True:
    for i in operator:
      print(i)
    task=input("what would you do? ")
    n2=float(input("\nwhat is the next number? "))
    task_function=operator[task]
    result=task_function(n1,n2)
    print(f"\n {n1} {task} {n2} = {result}")
  
    cont=input("would you continue? (y,n) ").lower()
    if cont=="y":
      n1=result
    else:
      keep_going=False
      calculater()

calculater()