import os

def find_replace_tags(directory, old_tag, new_tag):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # 👇 Find and replace tags
                    new_content = content.replace(f"#{old_tag}", f"#{new_tag}")
                    
                    # 👇 Write the updated content back to the file
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

# 👇 User inputs
directory = input("Enter the path to your Obsidian vault: ")
old_tag = input("Enter the old tag: ")
new_tag = input("Enter the new tag: ")

# 👇 Call the function
find_replace_tags(directory, old_tag, new_tag)