import pandas as pd
import csv

csv_path = 'csv/sra/liver/SraRunTable.csv'
data = pd.read_csv(csv_path, sep='\t')
filter_out = ["cancer", "carcinoma", "tumor", "tumour", "infection", "hepatitis", "Embryo", "fetal", "fetus", "organoid", "organoids",
              "knockout", "KO", "overexpression" "H3K4me3", "H3K27me3", "H3K27Ac", "H3K36me3", "H3K4me2", "H3K9ac", "H3K4me1",
              "H3-ChIP", "H3K9me3", "K27ac", "K27me3", "K4me1", "K4me3", "PolIII"]

mask = data.apply(lambda row: row.str.contains('|'.join(filter_out), case=False, na=False).any(), axis=1)

filtered_data = data[~mask]
filtered_output_file = 'csv/sra/liver/filtered_sra_experiments.csv'
filtered_data.to_csv(filtered_output_file, index=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar='\\')

removed_data = data[mask]
removed_output_file = 'csv/sra/liver/removed_sra_experiments.csv'
removed_data.to_csv(removed_output_file, index=False, sep='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
