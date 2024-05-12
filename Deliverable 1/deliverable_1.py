import seaborn as sns
anscombe = sns.load_dataset('anscombe')
anscombe
dataset1 = anscombe.iloc[0:11,0:3]
dataset1 = anscombe.iloc[11:22,0:3]
dataset1.plot.scatter(x='x',y='y')