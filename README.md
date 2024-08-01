# update_founder

A Python package to automatically find software updates of your repositories in GitHub

how does it work:

Step 1:
Go to your desired repository and create a file named version (don't give it a .txt extension)
And write your code in that version.

<picture>
  <img alt="write your code in that version." src="https://cdn.discordapp.com/attachments/1268584313763401749/1268585830574719046/6jR45QP.png?ex=66acf61f&is=66aba49f&hm=15be35caa7a1b2af851cafc61f7e4423170b14bcc005139293cbe96ae9dcdbf8&">
</picture>

Step 2:
Right click on the raw option and copy the link

<picture>
  <img alt="Right click on the raw option and copy the link" src="https://cdn.discordapp.com/attachments/1268584313763401749/1268587064237228062/EvHRGqn.png?ex=66acf745&is=66aba5c5&hm=0c9e77f0c0eb9060fc2ad7fb98941b6ff2fe4cf16220c6cdfe4d591fc21b91bc&">
</picture>

Step 3:
```py


# Set a new URL for version checking
set_url("https://raw.githubusercontent.com/Pytholearn/HAZARD-CHAMELEONS/main/version")

# Get the latest version information
latest_version = get_latest_version()

# Set the current version of the program
set_current_version("0.0.1")

# Check if the program is up to date
if is_up_to_date():
    print("The program is up to date!")
else:
    print("A new version is available. Downloading...")

    # Download and install the new version
    download("new_version.py")
    print("The program has been successfully updated to the latest version.")
```

Usage example:
```py
cwd = os.getcwd()
print(cwd)
AutoUpdate.set_url("https://raw.githubusercontent.com/Pytholearn/HAZARD-CHAMELEONS/main/version") # raw v link
download_link = "https://github.com/Pytholearn/HAZARD-CHAMELEONS.git" #your rep download link
AutoUpdate.set_current_version("1.1.2")
if not AutoUpdate.is_up_to_date():
    print("""New Update!""")

    print("Would you like to update your tool?")
    choice = input("If you like(Y) or you dont want to update (N)[>>>] ")
    if choice == "Y" or choice == "y":
    
        
        local_repo_path = os.path.join(cwd, "temp_repo")
        if not os.path.exists(local_repo_path):
            os.makedirs(local_repo_path)
        git.Repo.clone_from(download_link, local_repo_path)
        
        
        for root, dirs, files in os.walk(local_repo_path):
            relative_path = os.path.relpath(root, local_repo_path)
            for file in files:
                source_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(cwd, relative_path, file)
                if os.path.exists(dest_file_path):
                    os.remove(dest_file_path)  
                shutil.move(source_file_path, dest_file_path)  
            for dir in dirs:
                source_dir_path = os.path.join(root, dir)
                dest_dir_path = os.path.join(cwd, relative_path, dir)
                if not os.path.exists(dest_dir_path):
                    shutil.move(source_dir_path, dest_dir_path) 
        
        
        shutil.rmtree(local_repo_path)
        print("Update Complete!")
        time.sleep(2)
    elif choice == "n" or choice == "N":
        pass
else:
    print("Update Not Found!")
    time.sleep(2)

```

            ╔═════════════════════════HaZaRd═════════════════════════════╗
            ║        Youtube: https://www.youtube.com/@IIIHaZaRd         ║
            ║        Github: https://github.com/Pytholearn               ║
            ║        Discord: https://discord.gg/YU7jYRkxwp              ║
            ╚════════════════════════════════════════════════════════════╝


[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/qD8SXrRJbw) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/ili.hazard) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@iiihazard) 


