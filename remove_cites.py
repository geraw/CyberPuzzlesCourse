import re
import os

files_to_process = [
    r"c:/Users/geraw/courses/FormalVerificationMethods/00-intro.md",
    r"c:/Users/geraw/courses/FormalVerificationMethods/index.md"
]

def remove_cites(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove [cite_start]
    content = re.sub(r'\[cite_start\]', '', content)
    
    # Remove [cite: ...]
    # Assuming the content inside [cite: ...] does not contain ']'
    content = re.sub(r'\[cite:[^\]]*\]', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Processed {file_path}")

for file_path in files_to_process:
    remove_cites(file_path)
