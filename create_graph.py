import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/hg38_tf_cell_line_normal_experiments.csv', encoding='ISO-8859-1')
tf_column = df['Track type']
tf_counts = tf_column.value_counts()

# kördiagram
plt.figure(figsize=(8, 8))
plt.title('TF gyakoriság: "Normál sejtvonalas kísérletek"')
plt.pie(tf_counts, labels=tf_counts.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 6})
plt.axis('equal')
plt.show()
