import os
import shutil

# -----------------------------
# File Organiser
# -----------------------------
def organise_files():
    folder_path = input("Enter folder path (or press Enter for current folder): ") or os.getcwd()

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Others": []
    }

    for folder in file_types:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename != "smart_manager.py":
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

# -----------------------------
# File Search
# -----------------------------
def search_files():
    folder_path = input("Enter folder path (REQUIRED - do NOT press enter): ")
    keyword = input("Enter search keyword: ")

    valid_extensions = [".txt", ".py", ".md"]
    skip_dirs = ["__pycache__", ".git"]

    results = []

    print("\n🔍 Searching...\n")

    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:
            file_path = os.path.join(root, file)

            if not any(file.lower().endswith(ext) for ext in valid_extensions):
                continue

            # Check filename
            if keyword.lower() in file.lower():
                results.append(f"📄 Filename match: {file_path}")

            # Check file content
            try:
                with open(file_path, "r") as f:
                    for line_number, line in enumerate(f, start=1):
                        if keyword.lower() in line.lower():
                            results.append(f"🔍 Content match: {file_path} (line {line_number})")
                            break
            except:
                pass

    # Print results
    if results:
        for result in results:
            print(result)

        # Save to file
        with open("search_results.txt", "w") as file:
            for result in results:
                file.write(result + "\n")

        print("\n💾 Results saved to search_results.txt")
    else:
        print("No matches found.")

# -----------------------------
# Menu
# -----------------------------
def main_menu():
    while True:
        print("\n🧠 Smart File Manager")
        print("1. Organise Files")
        print("2. Search Files")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            organise_files()
        elif choice == "2":
            search_files()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# -----------------------------
# Run program
# -----------------------------
if __name__ == "__main__":
    main_menu()
