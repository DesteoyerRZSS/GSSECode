# Date: 06/12/2023
# Author: Ryan Zheng
# Assignment: Create a Numpys project
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("http://web.eecs.utk.edu/~smarz1/courses/cosc505/moderna.csv")

distinctDates = data['Week of Allocations'].drop_duplicates()
print(distinctDates)

sorted = data.groupby(['Week of Allocations'], sort=False).sum()

dates = []
for i in distinctDates:
    dates.append(i)

df = pd.DataFrame({
    'Week of Allocations': dates,
    '1st Dose Allocations': sorted.iloc[:, 1],
    '2nd Dose Allocations': sorted.iloc[:, 2]
})
print(df)
df.plot(x="Week of Allocations", y=["1st Dose Allocations", "2nd Dose Allocations"], xlabel='Week of Allocations', ylabel='Amount (Millions)', kind="bar")
plt.show()