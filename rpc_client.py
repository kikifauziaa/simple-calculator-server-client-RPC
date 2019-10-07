import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://192.168.43.49:8000')

num1 = float (input("Enter The First Number: "))
num2 = float (input("Enter The Second Number: "))
print ("A List Of Available Mathematical Operations \n")
print ("1.Multiple ")
print ("2.Divide ")
print ("3.Substract ")
print ("4.Add \n")
opr = int (input("Enter Your Choice (1,2,3,4): "))

if opr==1:
    print ("Result: ")
    print (proxy.Mul(num1,num2))
elif opr==2:
    print ("Result: ")
    print (proxy.Div(num1,num2))
elif opr==3:
    print ("Result: ")
    print (proxy.Sub(num1,num2))
elif opr==4:
    print ("Result: ")
    print (proxy.Add(num1,num2))
else:
    print ("\n Error : Mathematical Operations Input doesn't match With The List!")

