import matplotlib.pyplot as plt
days = ['Mon','Tue','Wed','Thu','Fri']
savings = [70,75,80,90,110]

plt.plot(days,savings,color='Blue',marker='o', linestyle='dashed',linewidth=2)
plt.title("My savings this week")
plt.xlabel("Day")
plt.ylabel("Savings")
plt.grid(True)
plt.ylim(0,110)
plt.show()


plt.bar(days,savings,color='orange')
plt.title("My savings this week")
plt.xlabel("Day")
plt.ylabel("Savings")
plt.grid(True)
plt.ylim(0,110)
plt.show()
