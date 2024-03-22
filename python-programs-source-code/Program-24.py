import matplotlib.pyplot as plt
import seaborn as sns
import random

# Generate random weight and height data for 20 persons
random.seed(42)
weights = [random.uniform(50, 100) for _ in range(20)]
heights = [random.uniform(150, 200) for _ in range(20)]

# Visualize the relationship using matplotlib and seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x=weights, y=heights, color='blue')
plt.title('Relationship between Weight and Height')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.grid(True)
plt.show()
