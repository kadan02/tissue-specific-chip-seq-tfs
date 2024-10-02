import pandas

data = pandas.read_csv('csv/hg38_filtered_experiments.csv', encoding='ISO-8859-1')
data_relevant = data[['Track type', 'Cell type class']]

organ_tf_counts = data_relevant.groupby('Cell type class')['Track type'].agg(lambda x: list(set(x))).reset_index()
organ_tf_counts['Total Unique TFs'] = organ_tf_counts['Track type'].apply(len)
organ_tf_counts['Track type'] = organ_tf_counts['Track type'].apply(lambda x: ', '.join(x))

print(organ_tf_counts)

organ_tf_counts.to_csv('unique_tfs_per_organ.csv', index=False)
