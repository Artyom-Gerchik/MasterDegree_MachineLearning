import os
from PIL import Image

class FolderManager:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def remove_corrupted_images(self):
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

        print("\nRemoving corrupted images...\n")
        counter = 1
        for subfolder in os.listdir(self.root_folder):
            subfolder_path = os.path.join(self.root_folder, subfolder)
            if os.path.isdir(subfolder_path):
                for root, dirs, files in os.walk(subfolder_path):
                    for file in files:
                        if file.lower().endswith(image_extensions):
                            file_path = os.path.join(root, file)
                            print(f"image number: {counter}")
                            try:
                                with Image.open(file_path) as img:
                                    img.verify()
                            except:
                                print(f"File removed: {file_path}")
                                os.remove(file_path)

                            counter += 1
        print("\nSuccessfully removed corrupted images\n")