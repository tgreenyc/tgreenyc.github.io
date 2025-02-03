import os
import re

# Set the directory where your HTML files are located
html_directory = r"C:\Users\Tim Green\Desktop\MickeyBaker\www.jazzandhotguitar.com"  # Change this to your actual folder path
stylesheet_link = '<link rel="stylesheet" href="../css/styles.css">'

# Regex patterns to remove inline styles
style_tag_pattern = re.compile(r'<style.*?>.*?</style>', re.DOTALL)
old_link_pattern = re.compile(r'<link[^>]*stylesheet[^>]*>', re.IGNORECASE)

def process_html_file(file_path):
    with open(file_path, "r", encoding="iso-8859-15") as file:
        content = file.read()
    
    # Remove existing <style> tags and <link> elements in <head>
    content = style_tag_pattern.sub("", content)
    content = old_link_pattern.sub("", content)

    # Ensure <head> exists and insert the new <link> tag
    if "<head>" in content:
        content = re.sub(r'(<head.*?>)', r'\1\n    ' + stylesheet_link, content, count=1)
    else:
        print(f"Warning: No <head> tag found in {file_path}, skipping.")

    # Save the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def update_all_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                print(f"Updating: {file_path}")
                process_html_file(file_path)

if __name__ == "__main__":
    update_all_html_files(html_directory)
    print("✅ All HTML files updated!")