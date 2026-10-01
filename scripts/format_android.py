import os
import yaml

input_path = "patches/imported_patch.yml"

if os.path.exists(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Load and normalize data to strip duplicate root keys
    data = yaml.safe_load(content)

    with open(input_path, "w", encoding="utf-8", newline="\n") as f:
        # Prepend the required Android header
        f.write("Version: 1.2\n")
        yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)
    
    print("Successfully formatted imported_patch.yml for Android compatibility.")
else:
    print(f"Error: {input_path} not found.")
