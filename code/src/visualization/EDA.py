import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
train_df = pd.read_csv("/Users/riyazachariah/Thermostability_Prediction/data/interim/updated_train.csv")
# Drop columns
train_df = train_df.drop(columns=['seq_id', 'data_source'])

# Display the data

# Swarm plot
sns.swarmplot(x="tm", y="pH", data=train_df)
plt.ylim(0, 14)
plt.yticks(np.arange(0, 14, 1))
plt.show()

# Box Plot
sns.boxplot(x='tm', data=train_df)
plt.show()

# Histogram
sns.histplot(x='tm', data=train_df)
plt.show()

# Density Plot
sns.kdeplot(data=train_df['tm'], fill=True)
plt.show()

# Heatmap
corr = train_df.corr()
sns.heatmap(corr, annot=True)
plt.show()

# Violin Plot
sns.violinplot(x='tm', data=train_df)
plt.show()

# Joint plot
sns.jointplot(x="tm", y="pH", data=train_df, kind="scatter")
plt.show()
