import numpy as np

class Task2Manager:

    @staticmethod
    def check_classes_balance(folder_images):
        images_counts = []

        for folder in folder_images:
            folder_images_count = len(folder['images'])
            print(f"Folder: {folder['folder']}, Count of images: {folder_images_count}")
            images_counts.append(folder_images_count)

        mean = np.mean(images_counts)
        std_dev = np.std(images_counts)
        
        print(f"\nMean: {mean}")
        print(f"Standard deviation: {std_dev}\n")

        if std_dev < 1.0:
            print("Classes balanced")
        else:
            print("Classes are not balanced")
