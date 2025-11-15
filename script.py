import os

root_dir = "."
readme_file = "README.md"

def generate_links(root):
    links = []
    for current_path, dirs, files in os.walk(root):
        # Skip .git and hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '.git']

        rel_path = os.path.relpath(current_path, root)
        if rel_path == ".":
            continue  # Skip root itself

        depth = rel_path.count(os.sep)  # For indentation
        indent = "    " * depth

        # Create clickable Markdown link
        github_link = f"./{rel_path}/"
        links.append(f"{indent}- {github_link}")
    return links

links = generate_links(root_dir)

with open(readme_file, "w", encoding="utf-8") as f:
    f.write("# Project Overview\n\n")
    f.write("## Folder Structure\n\n")
    for link in sorted(links):
        f.write(f"{link}\n")

print("README.md generated with clickable links and tree indentation!")