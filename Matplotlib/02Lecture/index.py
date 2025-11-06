import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(1, 6)
# y1 = x ** 2      # 1, 4, 9, 16, 25
# y2 = x ** 3      # 1 , 8, 27, 64, 125

# plt.figure(figsize=(10,4))   # Bigger canvas

# plt.subplot(1,2,1)   # (rows=1, cols=2, position=1)
# plt.plot(x, y1, marker="o", color="blue")
# plt.title("Square Numbers")

# plt.subplot(1,2,2)   # (rows=1, cols=2, position=2)
# plt.plot(x, y2, marker="s", color="green")
# plt.title("Cubic Numbers")

# plt.tight_layout()   # Avoid overlap
# plt.show()




# plt.plot([10, 20, 30, 40], [1, 4, 9, 16], marker="o")

# # Custom ticks
# plt.xticks([10, 20, 30, 40], labels=["Ten", "Twenty", "Thirty", "Forty"])
# plt.yticks([0, 5, 10, 15, 20])

# # Add grid
# plt.grid(True, linestyle="--", alpha=0.7)
# plt.title("Custom Ticks & Grid")
# plt.show()


x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y, marker="o")
plt.title("Annotations Example")

# Adding simple text
plt.text(2, 5, "Midpoint", color="red", fontsize=10)

# Adding annotation with arrow
plt.annotate("Peak", xy=(1,2), xytext=(2,6),
             arrowprops=dict(facecolor="black", shrink=0.01))

plt.show()




# categories = ["Pizza", "Burger", "Pasta", "Salad"]
# sales = [500, 300, 400, 250]

# plt.bar(categories, sales, color="orange")
# plt.title("Food Sales by Category")
# plt.xlabel("Menu Items")
# plt.ylabel("Sales")
# plt.show()
