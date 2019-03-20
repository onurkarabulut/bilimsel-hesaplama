#girilen tahmin aralıklarında köklerin yarıya bölme yöntemiyle bulunması
def f(x):
  return(x**2-4*x+3) #x**2 = x'in karesini alır

x1=int(input("baslangic tahmini: "))
x2=int(input("bitis tahmini: "))
if(f(x1)*f(x2)==0):
  print("tahminlerinizden biri denklemin kokudur")
elif(f(x1)*f(x2)>0):
  print("girdiginiz tek sayida kok yoktur")
else:
  for i in range(100):
    xr=(x1+x2)/2
    if(f(xr)==0):
      print("kok bulundu: ",xr,i)
      break
    elif(f(x1)*f(xr)<0):
      x2=xr
    else:
      x1=xr
    print(xr)
    
