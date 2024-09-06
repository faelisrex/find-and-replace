# Find and Replace Tags in Markdown Files

This script allows you to find and replace tags in all Markdown (`.md`) files within a specified directory. It is particularly useful for users of Obsidian or other Markdown-based note-taking applications who need to update tags across multiple files.

## Features

- Recursively searches through a directory for Markdown files.
- Replaces specified old tags with new tags.
- Handles file reading and writing with UTF-8 encoding.
- Provides error handling for file operations.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository or download the script:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the script:**

   ```sh
   python findReplaceTags.py
   ```

3. **Follow the prompts:**

   - Enter the path to your Obsidian vault (or the directory containing your Markdown files).
   - Enter the old tag you want to replace.
   - Enter the new tag you want to use.

## Example

```sh
Enter the path to your Obsidian vault: /path/to/your/vault
Enter the old tag: oldTag
Enter the new tag: newTag
```
