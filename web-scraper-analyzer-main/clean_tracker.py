import os
import shutil

folder = r"C:\Users\Aman\Desktop\New folder\personal_finance_tracker-main\personal_finance_tracker-main"

# 1. Delete LICENSE file
license_path = os.path.join(folder, "LICENSE")
if os.path.exists(license_path):
    os.remove(license_path)
    print("Deleted LICENSE")

# 2. Delete .git folder
git_path = os.path.join(folder, ".git")
if os.path.exists(git_path):
    shutil.rmtree(git_path)
    print("Deleted .git folder")

# 3. Clean Python files
python_files = ["launcher.py", "interactive_finance_tracker.py", "finance_tracker.py"]
for pf in python_files:
    p = os.path.join(folder, pf)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("Author: Saksham Lamsal\n", "")
        content = content.replace("Date: June 2025\n", "")
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Cleaned {pf}")

# 4. Clean setup.py
setup_path = os.path.join(folder, "setup.py")
if os.path.exists(setup_path):
    with open(setup_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    with open(setup_path, "w", encoding="utf-8") as f:
        for line in lines:
            if "url=" in line or "author=" in line or "author_email=" in line or "license=" in line or "License ::" in line or "project_urls=" in line or "Bug Reports" in line or "Source" in line or "Documentation" in line:
                continue
            f.write(line)
    print("Cleaned setup.py")

# 5. Clean README.md
readme = os.path.join(folder, "README.md")
if os.path.exists(readme):
    with open(readme, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(readme, "w", encoding="utf-8") as f:
        for line in lines:
            if "## 📄 License" in line:
                break  # Stop writing after License section starts
            if "git clone" not in line:
                f.write(line)
    print("Cleaned README.md")

print("Project is now clean and ready to be made your own!")
