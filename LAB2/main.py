from folder_manager import FolderManager
from task1 import Task1Manager
from task3 import Task3Manager
from task4 import Task4Manager

import os

# Large Dataset: C:\Users\bombr\OneDrive\Desktop\Machine_Learning\LAB1\Datasets\notMNIST_large
# Small Dataset: C:\Users\bombr\OneDrive\Desktop\Machine_Learning\LAB1\Datasets\notMNIST_small

class Main:
    def __init__(self):
        self.valid_choices = ['1', '2', '3', '4', '5']
        self.folder_images = []
        self.learning_set = []
        self.validate_set = []
        self.control_set = []

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
  
    def main_function(self):
        self.clear_console()    
        root_folder = input("Insert folder path: ")
        self.folder_images = FolderManager(r'%s' %root_folder).remove_corrupted_images()

        Task1Manager.create_and_learn_model(root_folder)
        Task3Manager.create_and_learn_model(root_folder)
        Task4Manager.create_and_learn_model(root_folder)

if __name__ == "__main__":
    main = Main()
    main.main_function()