import os

input_path = "patches/imported_patch.yml"

if os.path.exists(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip out any existing Version headers at the very top to prevent duplication
    lines = content.splitlines()
    cleaned_lines = []
    skip_header = False
    
    for i, line in enumerate(lines):
        if i < 5 and line.strip().startswith("Version:"):
            continue
        cleaned_lines.append(line)
        
    cleaned_content = "\n".join(cleaned_lines)

    # Write strictly as text: Exactly ONE Version: 1.2 header + raw untouched patch content
    with open(input_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("Version: 1.2\n")
        f.write(cleaned_content)
    
    print("Successfully prepended Version: 1.2 header as raw text safely.")
else:
    print(f"Error: {input_path} not found.")
