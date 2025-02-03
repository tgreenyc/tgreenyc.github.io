import os
import re

# Set the directory where your HTML files are located
html_directory = r"C:\Users\Tim Green\Desktop\MickeyBaker\www.jazzandhotguitar.com"  # Change this to your actual folder path
viewport_meta_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

# Regex pattern to check if the viewport meta tag already exists
viewport_meta_pattern = re.compile(r'<meta\s+name=["\']viewport["\'][^>]*>', re.IGNORECASE)

def process_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Check if the viewport meta tag already exists
    if not viewport_meta_pattern.search(content):
        # If it doesn't exist, add it inside the <head> section
        if "<head>" in content:
            content = re.sub(r'(<head.*?>)', r'\1\n    ' + viewport_meta_tag, content, count=1)
        else:
            print(f"Warning: No <head> tag found in {file_path}, skipping.")
    
        # Save the modified content back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Added viewport meta tag to: {file_path}")

def update_all_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                process_html_file(file_path)

if __name__ == "__main__":
    update_all_html_files(html_directory)
    print("✅ All HTML files updated!")
