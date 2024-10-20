import pandas as pd
import matplotlib.pyplot as plt

fusion = [1,2,3,4,5,6]
xyz = [3,4,5,6]
xticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
yticks = [1,2,3,4,5,6,7,8,9,10,11,12]
level, cardCount, combo = [], [], []


for f in fusion:
    for x in xyz:
        level.append(f + x)
        cardCount.append(f + x + x)
        combo.append(str(f) + "+" + str(x))

#plt.plot(cardCount, level, "s", markersize=15)
for c in range(len(combo)):
    plt.annotate(combo[c], (cardCount[c], level[c]), color="white", ha="center", va="center", size=7, bbox=dict(facecolor="black", edgecolor="black", pad=1.5))
    #textcoords="offset points",xytext=(0,0)
plt.xlabel("Card Count")
plt.ylabel("Level")
plt.xticks(xticks)
plt.yticks(yticks)
plt.xlim(cardCount[0]-1, cardCount[-1]+1)
plt.ylim(level[0]-1, level[-1]+1)
plt.grid()
plt.show()

