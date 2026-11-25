import matplotlib.pyplot as plt
days = ['Mon','Tue','Wed','Thu','Fri']
score = [70,75,60,80,95]

plt.plot(days,score)
plt.title("My scores this week")
plt.xlabel("Day")
plt.ylabel("Score")
plt.grid(True)
plt.ylim(0,100)
plt.show()

plt.plot(days,score,color='Blue',marker='o', linestyle='dashed',linewidth=2)
plt.title("My scores this week")
plt.xlabel("Day")
plt.ylabel("Score")
plt.grid(True)
plt.ylim(0,100)
plt.show()

plt.bar(days,score,color='orange')
plt.title("My scores this week")
plt.xlabel("Day")
plt.ylabel("Score")
plt.grid(True)
plt.ylim(0,100)
plt.show()