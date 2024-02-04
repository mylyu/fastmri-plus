import csv

# Path to the brain.csv file and brain_file_list.csv file
csv_file_path = "Annotations/brain.csv"
file_list_path = "Annotations/brain_file_list.csv"

# Create a set to store the files listed in the CSV file
annotated_files = set()

# Read the brain.csv file and extract the file names
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        file_name = row[0]
        if "normal" not in row[7].lower():
            annotated_files.add(file_name)
print(len(annotated_files))
# Read the brain_file_list.csv file
with open(file_list_path, "r") as file_list_file:
    file_list_reader = csv.reader(file_list_file)
    for file_name in file_list_reader:
        file_name = file_name[0]
        if file_name not in annotated_files:
            print(f"{file_name}")

print("Done!")
