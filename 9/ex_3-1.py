import matplotlib.pyplot as plot
import pandas as pd

plot.rcParams['font.family'] = "Hiragino Sans"

df = pd.read_csv("./9/09sales_data.csv")

plot.plot(df["Month"], df["Sales"], marker="o")
plot.title("Sales of Month")
plot.xlabel("Month")
plot.ylabel("Sales")

plot.show()
