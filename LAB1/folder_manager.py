import os

class FolderManager:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def find_images(self):
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        folder_images = []

        for subfolder in os.listdir(self.root_folder):
            subfolder_path = os.path.join(self.root_folder, subfolder)
            if os.path.isdir(subfolder_path):
                images = []
                for root, dirs, files in os.walk(subfolder_path):
                    for file in files:
                        if file.lower().endswith(image_extensions):
                            images.append(os.path.join(root, file))
                folder_images.append({'folder': subfolder, 'images': images})
        
        return folder_images