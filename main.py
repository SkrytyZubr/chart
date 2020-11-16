import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("kandydaci_utf8.csv", delimiter=";")
url = 'https://prezydent20200628.pkw.gov.pl/prezydent20200628/pl/kandydaci'
dfs = pd.read_html(url)

y = df["Nazwisko"]
x = df["Liczba głosów"]

df2 = df[["Wiek"]]

y1 = y.tolist()
x1 = x.tolist()
xy = dict(zip(y1, x1))
xy_1 = {}
xy_new = {}

def more_than_1(xy):
    for keys, values in xy.items():
        if values > 194254:
            xy_1.update({keys : (values / 1000000)})

def only_2nd_half(x1,y1):
    xy_new.update({y1[2]:x1[2]})
    xy_new.update({y1[8]:x1[8]})
    xy_new.update({"Pozostali":(sum(x1)-(x1[2]+x1[8]))})

# fig,a = plt.subplots(3,2)

ax1 = plt.subplot2grid((3, 8), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 8), (0, 3), colspan=2, rowspan=2)
ax3 = plt.subplot2grid((3, 8), (1, 0), colspan=2)
ax4 = plt.subplot2grid((3, 8), (0, 6), colspan=2, rowspan=2)
ax5 = plt.subplot2grid((3, 8), (2, 0), colspan=8)

#first chart

ax1.barh(y, (x/1000000), color=["red", "green", "blue"])
ax1.set_title("Wykres pierwszy (x1000000)")

#second chart

wedges, texts, autotexts = ax2.pie(x1, autopct="%.2f %%" ,textprops=dict(color="w"))
ax2.legend(wedges, y, title="Kandydaci", bbox_to_anchor=(0.9, 0, 0.5, 1))
ax2.set_title("Wykres drugi")

#third chart

more_than_1(xy)
xy_keys = list(xy_1.keys())
xy_values = list(xy_1.values())
ax3.barh(xy_keys, xy_values, color=["red", "green", "blue"])
ax3.set_title("Wykres trzeci, kandydaci którzy przekroczyli 1% (x1000000)")

#fourth chart

only_2nd_half(x1, y1)
xy_new_keys = list(xy_new.keys())
xy_new_values = list(xy_new.values())
ax4.pie(xy_new_values , labels = xy_new_keys, autopct = "%.2f %%")
ax4.set_title("Wykres kandydatów którzy przeszli do drugiej tury i pozostali łącznie.")

#fifth chart

ax5.hist(df2, bins = 10, range = (35, int(df2.max())), facecolor = "blue", edgecolor='b', linewidth=1, alpha = 0.5)
ax5.set_title("Wykres wieku kandydatów")

plt.show()







