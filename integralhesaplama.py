#integral hesaplama yontemleri
def f(x):
  return(x**2)
x1=4
x2=6

n=10 #araligin kac parcaya bolunecegi
h=(x2-x1)/n
integral=0
#kisakenar yontemi ile
for i in range(n):
  integral += f(x1+i*h)*h
print(integral)
#uzunkenar yontemi ile
integral=0
for i in range(1,n+1):
  integral += f(x1+i*h)*h
print(integral)
#orta nokta yontemi ile
integral=0
for i in range(n):
  integral += f(x1+h/2+i*h)*h
print(integral)
#alani yamuk parcalara ayirarak
integral=0
for i in range(n):
  integral += (f(x1+i*h)+f(x1+(i+1)*h))*h/2
print(integral)
