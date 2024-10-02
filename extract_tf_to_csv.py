import os
import csv


def extract_tf(metadata):
    for item in metadata.split(';'):
        if item.startswith("Name="):
            tf_name = item.split('%20(@')[0].replace('Name=', '').replace('%20', ' ')
            return tf_name
    return None


def process_bed_files(base_folder, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(['Organ', 'Tissue', 'Transcription Factors', 'Total Unique TFs'])

        for organ_folder in os.listdir(base_folder):
            organ_folder_path = os.path.join(base_folder, organ_folder)
            if os.path.isdir(organ_folder_path):
                # Egyedi TF-ek itt lesznek tárolva
                organ_tf_set = set()

                # Almappák iterálása
                for tissue_folder in os.listdir(organ_folder_path):
                    tissue_folder_path = os.path.join(organ_folder_path, tissue_folder)
                    if os.path.isdir(tissue_folder_path):
                        tf_list = []

                        # .bed fileok iterálása az almappákban
                        for bed_file in os.listdir(tissue_folder_path):
                            if bed_file.endswith('.bed'):
                                bed_file_path = os.path.join(tissue_folder_path, bed_file)
                                print(f"Processing bed file: {bed_file}")

                                # Bed file első sorának olvasása
                                with open(bed_file_path, 'r', encoding='utf-8') as infile:
                                    first_line = infile.readline().strip()
                                    columns = first_line.split('\t')
                                    if len(columns) > 3:
                                        tf_name = extract_tf(columns[3])
                                        if tf_name and tf_name not in tf_list:
                                            tf_list.append(tf_name)
                                            organ_tf_set.add(tf_name)

                        if tf_list:
                            tf_count = len(tf_list)
                            csv_writer.writerow([organ_folder, tissue_folder, ', '.join(tf_list), tf_count])
                        else:
                            csv_writer.writerow([organ_folder, tissue_folder, 'No TF', 0])

                organ_tf_count = len(organ_tf_set)
                csv_writer.writerow([organ_folder, 'NA', ', '.join(sorted(organ_tf_set)), organ_tf_count])


if __name__ == "__main__":
    base_folder = "data"
    output_file = "tf_list.csv"
    process_bed_files(base_folder, output_file)
