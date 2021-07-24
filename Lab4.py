import matplotlib.pyplot as plt

aA1 = 10
bA1 = 20
cA1 = 30
A1 = []

for x in range(50):
    if x <= aA1:
        A1.append(0)
    elif x <= bA1:
        A1.append((x-aA1)/(bA1-aA1))
    elif x <= cA1:
        A1.append((cA1-x)/(cA1-bA1))
    else:
        A1.append(0)

aA2 = 5
bA2 = 10
cA2 = 15
A2 = []

for x in range(50):
    if x <= aA2:
        A2.append(0)
    elif x <= bA2:
        A2.append((x-aA2)/(bA2-aA2))
    elif x <= cA2:
        A2.append((cA2-x)/(cA2-bA2))
    else:
        A2.append(0)

aA3 = 7.5
bA3 = 30
cA3 = 40
A3 = []

for x in range(50):
    if x <= aA3:
        A3.append(0)
    elif x <= bA3:
        A3.append((x-aA3)/(bA3-aA3))
    elif x <= cA3:
        A3.append((cA3-x)/(cA3-bA3))
    else:
        A3.append(0)

aA4 = 1
bA4 = 4
cA4 = 21
A4 = []

for x in range(50):
    if x <= aA4:
        A4.append(0)
    elif x <= bA4:
        A4.append((x-aA4)/(bA4-aA4))
    elif x <= cA4:
        A4.append((cA4-x)/(cA4-bA4))
    else:
        A4.append(0)

plt.plot(A1)
plt.plot(A2)
plt.plot(A3)
plt.plot(A4)
plt.show()