import os
import shutil

print("📂 File Organiser")

folder_path = input("Enter folder path (or press Enter for current folder): ")

if folder_path == "":
    folder_path = "."

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Others": []
}

# Create folders if they don't exist
for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Organise files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination = os.path.join(folder_path, folder, filename)
                shutil.move(file_path, destination)
                moved = True
                break

        if not moved:
            destination = os.path.join(folder_path, "Others", filename)
            shutil.move(file_path, destination)

print("✅ Files organised!")
