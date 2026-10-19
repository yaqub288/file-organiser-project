from pathlib import Path

print("======= File Organiser =======")

filename = input("Enter a filename: ").strip().lower()

if filename.endswith((".txt", ".docx", ".pdf")):
    category = "Documents"
elif filename.endswith((".jpg", ".png", ".jpeg")):
    category = "Pictures"
elif filename.endswith(".mp3"):
    category = "Audio"
elif filename.endswith(".mp4"):
    category = "Video"
elif filename.endswith(".md"):
    category = "Obsidian"
elif filename.endswith(".py"):
    category = "Python Projects"
else:
    category = "Other"

print(f"Category: {category}")

test_folder = Path("test_folder")

print(test_folder.exists())
print(list(test_folder.iterdir()))

for file in test_folder.iterdir():
    print(file.name)
