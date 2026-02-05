#71.2 Python Delete Folder
import os
try:
    os.rmdir("MyFolder")
    # os.rmdir("ParentFolder")
    print("Folder removed")
except FileNotFoundError:
    print("Folder not found")