import os
import yaml

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

    # Load and parse the YAML content safely
    try:
        data = list(yaml.safe_load_all(cleaned_content))
        if len(data) == 1:
            data = data[0]
    except Exception as e:
        print(f"Warning during yaml load: {e}")
        data = None

    with open(input_path, "w", encoding="utf-8", newline="\n") as f:
        # Write exactly ONE Version: 1.2 header at the very top
        f.write("Version: 1.2\n")
        if data is not None:
            yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)
        else:
            f.write(cleaned_content)
    
    print("Successfully formatted imported_patch.yml with a single Android header.")
else:
    print(f"Error: {input_path} not found.")
