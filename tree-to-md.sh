#!/bin/bash
# Generate clickable Markdown tree
echo "# Project Structure" > structure.md
echo "" >> structure.md
echo "\`\`\`text" >> structure.md
tree >> structure.md
echo "\`\`\`" >> structure.md
echo "" >> structure.md
echo "## Clickable Links" >> structure.md
echo "" >> structure.md
tree -df | sed 's/.*\///' | while read line; do
    echo "- ./$line" >> structure.md
done
