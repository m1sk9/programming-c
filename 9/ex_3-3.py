import matplotlib.pyplot as plot
import pandas as pd

plot.rcParams['font.family'] = "Hiragino Sans"

df = pd.read_csv("./9/09age_freq.csv")

plot.bar(df["Age"], df["Freq"], color="green", width=5)
plot.title("Frequency distribution of age")
plot.xlabel("Frequency")
plot.ylabel("Age")

plot.show()
