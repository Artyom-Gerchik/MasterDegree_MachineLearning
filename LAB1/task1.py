from PIL import Image

class Task1Manager:

    @staticmethod
    def show_images(folder_images):
        for folder in folder_images:
            img = Image.open(folder['images'][0])
            img.show()
