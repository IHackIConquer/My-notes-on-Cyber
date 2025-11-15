import os

# Root directory of your repo
root_dir = "."

# Output file
readme_file = "README.md"

with open(readme_file, "w", encoding="utf-8") as f:
    f.write("# Project Overview\n\n")
    f.write("## Folders\n\n")

    for item in sorted(os.listdir(root_dir)):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path) and item != ".git":
            # Create a clickable link
            f.write(f"- {item}/\n")

print(f"README.md generated with folder links!")