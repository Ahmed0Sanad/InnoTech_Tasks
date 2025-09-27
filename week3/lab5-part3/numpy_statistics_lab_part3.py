import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# NumPy Statistics LAB(5) - Part 3 Solutions

print("NumPy Statistics LAB(5) - Part 3: Data Analysis and Visualization")
print("=" * 70)

# 1. Student Exam Scores Analysis
print("\n1. Student Exam Scores Analysis")
print("-" * 40)
np.random.seed(42)
scores = np.random.normal(70, 10, 100)

# Calculate z-scores
z_scores = (scores - np.mean(scores)) / np.std(scores)
outliers = np.abs(z_scores) > 2

print(f"Mean score: {np.mean(scores):.2f}")
print(f"Standard deviation: {np.std(scores):.2f}")
print(f"Number of outliers (|z| > 2): {np.sum(outliers)}")
print(f"Outlier scores: {scores[outliers]}")

# Visualizations
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Dot plot with jitter
jitter = np.random.normal(0, 0.1, len(scores))
ax1.scatter(scores, jitter, alpha=0.6, c=['red' if o else 'blue' for o in outliers])
ax1.set_xlabel('Exam Scores')
ax1.set_ylabel('Jitter')
ax1.set_title('Dot Plot of Exam Scores')
ax1.grid(True, alpha=0.3)

# Histogram
ax2.hist(scores, bins=15, alpha=0.7, color='skyblue', edgecolor='black')
ax2.axvline(np.mean(scores), color='red', linestyle='--', label=f'Mean: {np.mean(scores):.1f}')
ax2.set_xlabel('Exam Scores')
ax2.set_ylabel('Frequency')
ax2.set_title('Score Distribution')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Z-scores
ax3.scatter(range(len(z_scores)), z_scores, c=['red' if o else 'blue' for o in outliers])
ax3.axhline(2, color='red', linestyle='--', alpha=0.7)
ax3.axhline(-2, color='red', linestyle='--', alpha=0.7)
ax3.set_xlabel('Student Index')
ax3.set_ylabel('Z-Score')
ax3.set_title('Z-Scores (Outliers in Red)')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 2. Fruit Sales Distribution
print("\n2. Fruit Sales Distribution")
print("-" * 40)
np.random.seed(42)
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
sales = np.random.randint(50, 200, size=5)
explode = [0.1 if s == max(sales) else 0 for s in sales]

print(f"Sales data: {dict(zip(fruits, sales))}")
print(f"Highest selling fruit: {fruits[np.argmax(sales)]} ({max(sales)} units)")

plt.figure(figsize=(8, 8))
plt.pie(sales, labels=fruits, explode=explode, autopct='%1.1f%%', 
        startangle=90, colors=['red', 'yellow', 'orange', 'purple', 'pink'])
plt.title('Fruit Sales Distribution')
plt.show()

# 3. Temperature vs. Ice Cream Sales
print("\n3. Temperature vs. Ice Cream Sales")
print("-" * 40)
np.random.seed(42)
temp = np.linspace(20, 35, 30)
sales = 50 + 2 * temp + np.random.normal(0, 5, 30)

# Calculate correlation
correlation = np.corrcoef(temp, sales)[0, 1]
r_squared = correlation ** 2

# Regression line
slope, intercept = np.polyfit(temp, sales, 1)
line = slope * temp + intercept

print(f"Pearson correlation coefficient: {correlation:.3f}")
print(f"R-squared: {r_squared:.3f}")
print(f"Regression equation: Sales = {slope:.2f} * Temp + {intercept:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(temp, sales, alpha=0.7, color='blue', label='Data points')
plt.plot(temp, line, color='red', linewidth=2, label=f'Regression line (R²={r_squared:.3f})')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales ($)')
plt.title('Temperature vs. Ice Cream Sales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 4. Income Distribution Across Professions
print("\n4. Income Distribution Across Professions")
print("-" * 40)
np.random.seed(42)
engineers = np.random.exponential(80000, 100) + 40000
teachers = np.random.normal(55000, 8000, 100)
artists = np.random.lognormal(10.5, 0.4, 100)

incomes = [engineers, teachers, artists]
professions = ['Engineers', 'Teachers', 'Artists']

# Calculate statistics
for i, (prof, income) in enumerate(zip(professions, incomes)):
    print(f"{prof}:")
    print(f"  Median: ${np.median(income):,.0f}")
    print(f"  IQR: ${np.percentile(income, 75) - np.percentile(income, 25):,.0f}")
    print(f"  Mean: ${np.mean(income):,.0f}")

plt.figure(figsize=(10, 6))
box_plot = plt.boxplot(incomes, labels=professions, patch_artist=True)
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
plt.ylabel('Income ($)')
plt.title('Income Distribution Across Professions')
plt.grid(True, alpha=0.3)
plt.show()

# 5. Study Hours vs. Exam Scores Regression
print("\n5. Study Hours vs. Exam Scores Regression")
print("-" * 40)
np.random.seed(42)
hours = np.random.uniform(1, 10, 50)
scores = 30 + 7 * hours + np.random.normal(0, 5, 50)

# Regression analysis
slope, intercept = np.polyfit(hours, scores, 1)
line = slope * hours + intercept
correlation = np.corrcoef(hours, scores)[0, 1]
r_squared = correlation ** 2

print(f"Regression equation: Score = {slope:.2f} * Hours + {intercept:.2f}")
print(f"R-squared: {r_squared:.3f}")
print(f"Correlation: {correlation:.3f}")

plt.figure(figsize=(10, 6))
plt.scatter(hours, scores, alpha=0.7, color='green')
plt.plot(sorted(hours), slope * np.array(sorted(hours)) + intercept, 
         color='red', linewidth=2, label=f'R² = {r_squared:.3f}')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Study Hours vs. Exam Scores')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 6. Website Traffic Analysis
print("\n6. Website Traffic Analysis")
print("-" * 40)
np.random.seed(42)
traffic = np.random.poisson(lam=50, size=744)  # 31 days * 24 hours

# Calculate z-scores
z_scores = (traffic - np.mean(traffic)) / np.std(traffic)
anomalies = np.abs(z_scores) > 3

print(f"Mean traffic: {np.mean(traffic):.1f} visits/hour")
print(f"Standard deviation: {np.std(traffic):.1f}")
print(f"Number of anomalies (|z| > 3): {np.sum(anomalies)}")
print(f"Peak traffic hours: {traffic[anomalies]}")

plt.figure(figsize=(12, 8))

# Histogram
plt.subplot(2, 1, 1)
plt.hist(traffic, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(np.mean(traffic), color='red', linestyle='--', label=f'Mean: {np.mean(traffic):.1f}')
plt.xlabel('Hourly Visits')
plt.ylabel('Frequency')
plt.title('Website Traffic Distribution')
plt.legend()
plt.grid(True, alpha=0.3)

# Time series with anomalies
plt.subplot(2, 1, 2)
plt.plot(traffic, alpha=0.7, color='blue')
plt.scatter(np.where(anomalies)[0], traffic[anomalies], color='red', s=50, label='Anomalies')
plt.xlabel('Hour')
plt.ylabel('Visits')
plt.title('Website Traffic Over Time (Anomalies in Red)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 7. Advertising Spend vs. Revenue
print("\n7. Advertising Spend vs. Revenue")
print("-" * 40)
np.random.seed(42)
spend = np.linspace(1000, 10000, 12)
revenue = 5000 + 2.5 * spend + np.random.normal(0, 1000, 12)

# Statistical analysis
correlation, p_value = stats.pearsonr(spend, revenue)
slope, intercept = np.polyfit(spend, revenue, 1)

print(f"Pearson correlation: {correlation:.3f}")
print(f"P-value: {p_value:.4f}")
print(f"Regression: Revenue = {slope:.2f} * Spend + {intercept:.0f}")

plt.figure(figsize=(10, 6))
plt.scatter(spend, revenue, s=100, alpha=0.7, color='purple')
plt.plot(spend, slope * spend + intercept, color='red', linewidth=2)
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Revenue ($)')
plt.title(f'Advertising Spend vs. Revenue (R = {correlation:.3f})')
plt.text(0.05, 0.95, f'R = {correlation:.3f}\nP = {p_value:.4f}', 
         transform=plt.gca().transAxes, bbox=dict(boxstyle='round', facecolor='white'))
plt.grid(True, alpha=0.3)
plt.show()

# 8. Movie Genre Popularity
print("\n8. Movie Genre Popularity")
print("-" * 40)
np.random.seed(42)
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance']
tickets = np.random.randint(5000, 30000, size=6)
min_idx = np.argmin(tickets)
explode = [0.1 if i == min_idx else 0 for i in range(len(genres))]

print(f"Ticket sales: {dict(zip(genres, tickets))}")
print(f"Least popular genre: {genres[min_idx]} ({tickets[min_idx]} tickets)")

plt.figure(figsize=(10, 8))
plt.pie(tickets, labels=genres, explode=explode, autopct='%1.1f%%', 
        startangle=90, colors=plt.cm.Set3(np.linspace(0, 1, len(genres))))
plt.title('Movie Genre Popularity (Least Popular Highlighted)')
plt.show()

# 9. Housing Price Analysis
print("\n9. Housing Price Analysis")
print("-" * 40)
np.random.seed(42)
suburban = np.random.normal(350000, 50000, 100)
urban = np.random.lognormal(12.8, 0.3, 100)
rural = np.random.exponential(250000, 100) + 150000

neighborhoods = [suburban, urban, rural]
names = ['Suburban', 'Urban', 'Rural']

# Statistics
for name, prices in zip(names, neighborhoods):
    print(f"{name}:")
    print(f"  Median: ${np.median(prices):,.0f}")
    print(f"  IQR: ${np.percentile(prices, 75) - np.percentile(prices, 25):,.0f}")
    print(f"  Mean: ${np.mean(prices):,.0f}")

plt.figure(figsize=(10, 6))
box_plot = plt.boxplot(neighborhoods, labels=names, patch_artist=True)
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
plt.ylabel('House Price ($)')
plt.title('Housing Price Distribution by Neighborhood')
plt.grid(True, alpha=0.3)
plt.show()

# 10. Athlete Performance: Age vs. Speed
print("\n10. Athlete Performance: Age vs. Speed")
print("-" * 40)
np.random.seed(42)
age = np.random.randint(18, 40, 40)
speed = 10 - 0.15 * age + np.random.normal(0, 0.5, 40)

# Analysis
correlation = np.corrcoef(age, speed)[0, 1]
slope, intercept = np.polyfit(age, speed, 1)
r_squared = correlation ** 2

print(f"Correlation coefficient: {correlation:.3f}")
print(f"R-squared: {r_squared:.3f}")
print(f"Regression: Speed = {slope:.3f} * Age + {intercept:.2f}")
print(f"Interpretation: {'Strong' if abs(correlation) > 0.7 else 'Moderate' if abs(correlation) > 0.5 else 'Weak'} negative correlation")

plt.figure(figsize=(10, 6))
plt.scatter(age, speed, alpha=0.7, color='orange', s=60)
plt.plot(sorted(age), slope * np.array(sorted(age)) + intercept, 
         color='red', linewidth=2, label=f'R² = {r_squared:.3f}')
plt.xlabel('Age (years)')
plt.ylabel('Sprint Speed (m/s)')
plt.title('Athlete Age vs. Sprint Speed')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n" + "=" * 70)
print("Analysis Complete!")