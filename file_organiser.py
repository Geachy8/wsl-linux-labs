import os
import shutil

print("📂 File Organiser")

folder_path = input("Enter folder path (or press Enter for current folder): ")

if folder_path == "":
    folder_path = "."

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Others": []
}

for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

for filename in os.listdir(folder_path):
    if filename == "file_organiser.py":
        continue

    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination = os.path.join(folder_path, folder, filename)
                print(f"Moving {filename} → {folder}")
                shutil.move(file_path, destination)
                moved = True
                break

        if not moved:
            destination = os.path.join(folder_path, "Others", filename)
            print(f"Moving {filename} → Others")
            shutil.move(file_path, destination)

print("✅ Files organised!")
