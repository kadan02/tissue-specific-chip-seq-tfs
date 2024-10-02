import os
import glob


def split_bed_sra(input_file, output_folder):
    sra_files = {}

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            columns = line.strip().split('\t')
            if len(columns) > 3:
                metadata = columns[3].split(';')

                # Metadata oszlopban az SRA ID megkeresése
                sra_id = None
                for item in metadata:
                    if item.startswith("ID="):
                        sra_id = item.split('=')[1]
                        break

                # Ha megvan az ID, a sor kiírása az adott ID nevével rendelkező fájlba
                if sra_id:
                    output_file_path = os.path.join(output_folder, f'{sra_id}.bed')
                    if sra_id not in sra_files:
                        sra_files[sra_id] = open(output_file_path, 'w', encoding='utf-8')
                    sra_files[sra_id].write(line)
            # else:
                # print(f"Sor kihagyása nem megfelelő számú oszlopok miatt: {line.strip()}")

    for sra_id in sra_files:
        sra_files[sra_id].close()


# Egyszerre több fájl feldolgozása. A "Oth.Neu.05.AllAg.Microglia.bed" adatai például a /Neu/Microglia mappába
# lennének írva
for bed_file in glob.glob("Oth.*.05.AllAg.*.bed"):
    parts = bed_file.split(".")
    cell_group = parts[1]
    cell_type = parts[4].replace('.bed', '')
    folder_name = os.path.join(cell_group, cell_type)
    split_bed_sra(bed_file, folder_name)

    print(f"{bed_file} feldolgozva. output mappa: {folder_name}")
