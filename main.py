from pathlib import Path
import shutil


print("======= File Organiser =======")

test_folder = Path("test_folder")

print(test_folder.exists())
print(list(test_folder.iterdir()))

files_to_organise = []

for file in test_folder.iterdir():
    if not file.is_file():
        continue

    print(file.name)

    if file.suffix.lower() in (".txt", ".docx", ".pdf"):
        category = "Documents"
    elif file.suffix.lower() in (".jpg", ".png", ".jpeg"):
        category = "Pictures"
    elif file.suffix.lower() == ".mp3":
        category = "Audio"
    elif file.suffix.lower() == ".mp4":
        category = "Video"
    elif file.suffix.lower() == ".md":
        category = "Obsidian"
    elif file.suffix.lower() == ".py":
        category = "Python Projects"
    else:
        category = "Other"

    print(f"Category: {category}")
    category_folder = test_folder / category

    print(f"{file.name} --> {category_folder.name}")

    files_to_organise.append((file, category_folder))


organise = input("Would you like the files to be organised (yes/no)").strip().lower()

if organise == "yes":
    for source, destination in files_to_organise:
        destination.mkdir(exist_ok=True)
        shutil.move(str(source), str(destination))
else:
    print("Not organising files...")
