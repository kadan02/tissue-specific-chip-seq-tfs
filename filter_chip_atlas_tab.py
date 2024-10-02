import pandas

table = pandas.read_csv('ChipAtlasExperimentList.tab', sep='\t', header=None, on_bad_lines='skip')

filtered_tab = table[
    (table[1] == 'hg38') &
    (table[2] == 'TFs and others')
]

filtered_tab.to_csv('hg38_TF_all_experiments.csv', index=False)
print(filtered_tab.head())
