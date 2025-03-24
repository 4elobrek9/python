import os
import shutil
for filename in os.listdir("."):
    if filename.endswith(".txt"):
        shutil.move(filename, "text_files")