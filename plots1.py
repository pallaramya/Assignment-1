import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("averages.csv")

# Function to create a line plot
def create_line_plot(data):
    plt.figure(figsize=(10, 6))
    for party in data['party'].unique():
        party_data = data[data['party'] == party]
        plt.plot(party_data['votes'], label=party)
    plt.xlabel('Votes')
    plt.ylabel('Agree Percentage')
    plt.title('Line Plot of Votes vs Agree Percentage by Party')
    plt.legend()
    plt.grid(True)
    plt.show()

def linePlot(data):
    plt.plot(sorted(data['agree_pct']))
    plt.plot(sorted(data['predicted_agree']))
    plt.ylabel('percentage')
    plt.title('agree_pct vs predicted_agree')
    plt.legend()
    plt.grid(True)
    plt.show()
# Function to create a scatter plot
def create_scatter_plot(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['votes'], data['agree_pct'], c=data['net_trump_vote'], cmap='viridis')
    plt.colorbar(label='Net Trump Vote')
    plt.xlabel('Votes')
    plt.ylabel('Agree Percentage')
    plt.title('Scatter Plot of Votes vs Agree Percentage with Net Trump Vote Color Mapping')
    plt.grid(True)
    plt.show()

# Function to create a bar chart
def create_bar_chart(data):
    party_counts = data['party'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(party_counts.index, party_counts.values)
    plt.xlabel('Party')
    plt.ylabel('Count')
    plt.title('Bar Chart of Party Counts')
    plt.grid(axis='y')
    plt.show()

# Call the functions to generate the visualizations
create_line_plot(data)
create_scatter_plot(data)
create_bar_chart(data)
linePlot(data)