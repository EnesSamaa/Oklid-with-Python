import math


x1=int(input("x1 değerini giriniz :"))
y1=int(input("y1 değerini giriniz :"))
x2=int(input("x2 değerini giriniz :"))
y2=int(input("y2 değerini giriniz :"))
Points=[(x1,y1),(x2,y2)]
cevap='evet'
while cevap=='evet':
    cevap=input("başka nokta eklemek ister misiniz?")
    
    if cevap=='evet':
        x=input("x değerini giriniz :")
        y=input("y değerini giriniz :")
        Points.append((x, y))
    else :break


i=0
for a in Points[i]:
    print(f"koordinat düzlemindeki {i}. noktanın koordinatları :{Points[i]}")
    i+=1
    if i==len(Points):
        break




d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"Girilen iki nokta arasındaki uzaklık {d}")