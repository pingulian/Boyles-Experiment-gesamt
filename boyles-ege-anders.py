Volume=[1.0,1.5,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0,16.0,18.0,20.0,24.0,28.0,32.0]
Pressure=[29.750,19.125,14.375,9.500,7.125,5.625,4.875,4.250,3.750,3.375,3.000,2.625,2.250,2.000,1.875,1.750,1.500,1.375,1.250]
PV=[ ]
abweichung=input("Abweichung in Prozent")
m=0
def prozent(prozent, ganz):
    return (prozent*ganz)/100
nummer=len(Volume)
for y in range(nummer):
    V=Volume[y]
    P=Pressure[y]
    x=P*V
    PV.append(x)
    m+=x
mittelwert=m/nummer
intervall1=prozent(100-int(abweichung),mittelwert)
intervall2=prozent(100+int(abweichung),mittelwert)
for b in range(nummer):
    if (PV[b]>=intervall1) and (PV[b]<=intervall2):
        c=True
    else:
        c=False
print("Liste von P*V:",PV)
print("Mittelwert von Liste P*V:",mittelwert)
if (c==True):
    print("P*V ist konstant")
else:
    print("P*V ist nicht konstant")
