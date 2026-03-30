import os

print("🔍 File Search Tool")

folder = input("Enter folder path: ")
keyword = input("Enter search keyword: ")

# Only search these file types
valid_extensions = [".txt", ".py", ".md"]

# Skip these folders
skip_dirs = ["__pycache__", ".git"]

for root, dirs, files in os.walk(folder):
    # Remove unwanted directories
    dirs[:] = [d for d in dirs if d not in skip_dirs]

    for file in files:
        file_path = os.path.join(root, file)

        # Only check valid file types
        if not any(file.lower().endswith(ext) for ext in valid_extensions):
            continue

        # Check filename
        if keyword.lower() in file.lower():
            print(f"📄 Found in filename: {file_path}")

        # Check inside file
        try:
            with open(file_path, "r") as f:
                for line_number, line in enumerate(f, start=1):
                    if keyword.lower() in line.lower():
                        print(f"🔍 Found in content: {file_path} (line {line_number})")
                        break
        except:
            pass
