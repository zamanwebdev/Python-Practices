import os

# Ask user for folder name
folder_name = input("Enter folder name you want to create: ")

try:
    # Create folder
    os.makedirs(folder_name, exist_ok=True)
    print(f"✅ Folder '{folder_name}' created successfully!")
except Exception as e:
    print("❌ Error:", e)
