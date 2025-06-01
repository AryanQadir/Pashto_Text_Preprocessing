import matplotlib.pyplot as plt

# Module names and their usage frequencies (as percentages)
modules = ['Normalization', 'Tokenization', 'Stop-word Removal', 'Stemming', 'POS Tagging']
usage_percentages = [98, 95, 90, 85, 80]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(modules, usage_percentages, color='#4682B4', edgecolor='black')
plt.ylim(0, 100)
plt.ylabel('Usage Frequency (%)')
plt.title('Figure X: Usage Frequency of NLP Preprocessing Modules in Pashto (TPTLP Model)')

# Annotate each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height - 5, f'{height}%', ha='center', va='bottom', color='white', fontsize=11, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Figure_X_TPTLP_Usage_Frequency.png')
plt.show()
