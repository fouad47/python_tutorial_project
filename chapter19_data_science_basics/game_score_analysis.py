# Pandas is a powerful toolbox for reading tables of data (like Excel or CSV).
import pandas as pd

# Matplotlib is a toolbox for drawing graphs.
import matplotlib.pyplot as plt

print("Loading student scores data...")

# We use pandas to read the CSV file and turn it into a DataFrame (a data table).
df = pd.read_csv("scores.csv")

print("\nHere is the data table:")
# This prints the whole table neatly!
print(df)

print("\nCalculating average score...")
# We select the "Score" column, and use .mean() to find the average.
average = df["Score"].mean()
print("The average score is:", average)

print("\nWho got the highest score?")
# We select the "Score" column, and use .max() to find the biggest number.
highest = df["Score"].max()
print("The highest score is:", highest, "🏆")

print("\nClose the graph window to finish the program.")

# We tell pandas to draw a 'bar' chart. The x-axis is Student, the y-axis is Score.
df.plot(kind='bar', x='Student', y='Score', color='skyblue')

# We add a title and labels to the chart.
plt.title("Student Game Scores")
plt.ylabel("Score")

# Finally, we show the chart on the screen!
plt.show()
