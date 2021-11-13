import matplotlib.pyplot

x = [100, 200, 300, 400, 500, 600]
y1 = [10, 20, 30, 50, 80, 130]
y2 = [10, 15, 30, 45, 60, 75]

fig = matplotlib.pyplot.figure()

# 1行2列に分割した中の1(左側)
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y1, marker="o", color="red", linestyle="--")

# 1行2列に分割した中の2(右側)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y2, marker="v", color="blue", linestyle=":")

# average = input('Enter number: ')
# standardDeviation = input('Enter number: ')

print("Hello, I'm Python!")
matplotlib.pyplot.show()
