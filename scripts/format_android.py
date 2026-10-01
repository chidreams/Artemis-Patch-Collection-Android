import os
import yaml

input_path = "patches/imported_patch.yml"

if os.path.exists(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Use safe_load_all to handle large or multi-document patch files safely
    try:
        data = list(yaml.safe_load_all(content))
        # If it's a single document list/dict, unwrap it if necessary
        if len(data) == 1:
            data = data[0]
    except Exception as e:
        print(f"Warning during yaml load, attempting raw dump: {e}")
        data = None

    with open(input_path, "w", encoding="utf-8", newline="\n") as f:
        # Prepend the required Android header
        f.write("Version: 1.2\n")
        if data is not None:
            yaml.safe_dump(data, f, sort_keys=False, default_flow_style=False)
        else:
            # Fallback to writing original content cleanly with UNIX line endings if parse failed
            f.write(content)
    
    print("Successfully formatted imported_patch.yml for Android compatibility.")
else:
    print(f"Error: {input_path} not found.")
