import pandas as pd
import csv

csv_path = 'csv/Liver/SraRunTable.csv'
data = pd.read_csv(csv_path, sep='\t', low_memory=False)
filter_out = ["cancer", "carcinoma", "tumor"]

mask = data.apply(lambda row: row.astype(str).str.contains('|'.join(filter_out), case=False, na=False).any(), axis=1)

filtered_data = data[~mask]
filtered_output_file = 'filtered_sra_experiments1.csv'
filtered_data.to_csv(filtered_output_file, index=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar='\\')

removed_df = data[mask]
removed_output_file = 'removed_sra_experiments1.csv'
removed_df.to_csv(removed_output_file, index=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
