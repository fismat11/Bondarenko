import matplotlib.pyplot as plt
import numpy as np
with open("data.txt", "r") as file:
    lst = file.readlines()
    alls = list(map(lambda x: int(x[:-1]), lst[:-1]))
    alls.append(int(lst[-1]))
with open("settings.txt", "r") as settings:
    lst = settings.readlines()
    perevod = list(map(lambda x: float(x[:-1]), lst[:-1]))
    perevod.append(float(lst[-1]))
alls = np.array(alls)
alls = alls * perevod[0]
n = len(alls)
print(alls[-2], alls[-1])
print(perevod)

plt.figure(figsize=(8, 6), dpi=200)
plt.title("Процесс заряда и разряда конденсатора в $RC$-цепочке")
plt.minorticks_on()
plt.grid(which="major")
plt.grid(which="minor", color="#EEEEEE", linewidth=1)
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
x = [_ * perevod[1] for _ in range(n)]
plt.plot(x, alls, color="orange", marker="o", markersize=0.3, label="$V(t)$")
plt.scatter([x[i] for i in range(0, len(x), 20)], [alls[i] for i in range(0, len(alls), 20)], color="orange")
plt.legend()
plt.xlim([0, 10])
plt.ylim([0, 3.5])
time_zar = x[alls.argmax()]
time_razr = x[-1] - time_zar
plt.text(6, 2.8, f"Время заряда: {str(time_zar)} сек")
plt.text(6, 2.5, f"Время разряда: {str(round(time_razr, 2))} сек")
plt.show()