import os

folder_path = "path/to/your/folder"

start_number = 1000
files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
files.sort(key=lambda x: int(x.split(".")[0]))

for i, file in enumerate(files, start=start_number):
    old_file_path = os.path.join(folder_path, file)
    new_file_name = f"{i}.csv"
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)

print("Files renamed successfully!")