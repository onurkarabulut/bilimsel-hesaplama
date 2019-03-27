#sekant yontemi
def f(x):
  return (x**2-4*x+3)

x1=int(input("baslangic degeri: "))
x2=int(input("bitis degeri: "))
if(f(x1)*f(x2)==0):
  print("girdiginiz degerlerden biri kok")
else:
  while(abs(f(x2)-f(1)>0.01)):#for i in range(50):
    x3=x1-f(x1)*(x2-x1)/(f(x2)-f(x1))
    x1,x2=x2,x3
    if(x1==x2): # if(f(x1)==f(x2)):
      break
  print(x1,x2,f(x1),f(x2))
