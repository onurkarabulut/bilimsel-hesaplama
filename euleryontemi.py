#euler yontemi
def f(x,y):
    return -y/x
y4=3/4
h=float(input("h degerini giriniz: "))
ys=int(input("y son degerini gir: "))
def euler(h,y4,ys):
    for i in range(4,ys):
        y4=y4-y4/i*h
    return y4

print(euler(h,y4,ys))
