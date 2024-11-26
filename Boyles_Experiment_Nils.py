v = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0]
p = [29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250]
pv = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
abweichung_von_avg = [0,1]


for i in range(0, 19):
    c = v[i] * p[i]
    pv[i] = c

avg = sum(pv)/19
minpv = min(pv)
maxpv = max(pv)

def abweichung_max (avg, minpv, maxpv):
    abweichung_von_avg [0] = abs(avg - minpv)
    abweichung_von_avg [1] = abs(avg - maxpv)
    return max(abweichung_von_avg)


print("Max Wert:", maxpv)
print("Min Wert:", minpv)
print("Durschschnitt", avg)
print("Max Abweichung von Duchschnitt:", abweichung_max(avg, minpv, maxpv))
if abweichung_max(avg, minpv, maxpv) < 10:
    print("p*v ist konstant!")
else:
    print("p*v ist nicht konstant")
