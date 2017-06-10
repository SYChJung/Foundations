# Foundations

## Subhead

- Sungyong Chung
- Lede 2017
- Homework and stuff for foundation

Code for Lede Python 2017  Foundations class

1.
WHA_group_dict = dict(list(WHA_group))
fig_Witbier    = WHA_group_dict['Witbier'].dropna()
fig_Hefeweizen = WHA_group_dict['Hefeweizen'].dropna()
fig_APWA       = WHA_group_dict['American Pale Wheat Ale'].dropna()
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()
for a in [fig_Witbier, fig_Hefeweizen, fig_APWA]:
    sns.distplot(a, bins=range(0, 66, 3), ax=ax, kde=False)
ax.set_xlim([0, 66])

2.
WHA_group_list = [ group.dropna()  for key,group in list(WHA_group) ]
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()
for a in WHA_group_list:
    sns.distplot(a, bins=range(0, 66, 3), ax=ax, kde=False)
ax.set_xlim([0, 66])

2-4
0-ex2
# 51-115-0
# beer	30-83
# dog	34-70
# https://tribecafilm.com/filmguide?letter=a
	- 	4-9
# html exercise : https://www.w3schools.com/tags/ref_byfunc.asp