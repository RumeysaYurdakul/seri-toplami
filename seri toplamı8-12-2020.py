#t=5+8+11+14+........+k>1000
#olmasını sağlayan en küçük k sayısı nedir?



t=5 #toplamın ilk değeri
k=8 #ilk eklenecek terim 
while t<=1000:    #t binden küçük eşit olduğu sürece toplamaya devam et
     t=t+k
     k=k+3

print("istenen k değeri=",k-3)#döngü çıkışında fazladan +3 yapıldığı için
                              #sonuç azaltılmalı




#sonucun sağlaması
t2=5
for i in range (8,78,3):
     t2=t2+i
print(t2)  #1025: 77 eklendiğinde 1000 değeri aşıldı doğru!
