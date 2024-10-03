from folder_manager import FolderManager

from task1 import Task1Manager
from task2 import Task2Manager
from task3 import Task3Manager
from task4 import Task4Manager


import os

class Main: # D:\DOWNLOADS\notMNIST_small.tar\notMNIST_small  D:\DOWNLOADS\notMNIST_large.tar\notMNIST_large
    def __init__(self):
        self.valid_choices = ['1', '2', '3', '4', '5']
        self.folder_images = []
        self.learning_set = []
        self.validate_set = []
        self.control_set = []


    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def handle_choice(self, choice):
        if choice == '1':
            print("\nTask 1. Showing some pictures!\n")
            Task1Manager.show_images(self.folder_images)
        elif choice == '2':
            print("\nTask 2. Checking classes for balance\n")
            Task2Manager.check_classes_balance(self.folder_images)
        elif choice == '3':
            print("\nTask 3. Separating data into 3 sets\n")
            self.learning_set, self.validate_set, self.control_set = Task3Manager.separate_images_into_sets(self.folder_images)
        elif choice == '4':
            if len(self.learning_set) == 0:
                print("Sets are empty, first try Task 3!")
            else:
                print("\nTask 4. Checking sets for duplicates\n")
                Task4Manager.check_sets_duplicates(
                    self.learning_set,
                    self.validate_set,
                    self.control_set
                )
        elif choice == '5':
            if len(self.learning_set) == 0:
                print("Sets are empty, first try Task 3!")
            else:
                print(213)
            
    def main_function(self):
        self.clear_console()    
        root_folder = input("Insert folder path: ")
        self.folder_images = FolderManager(r'%s' %root_folder).find_images()

        if self.folder_images.count != 0:
            while True:
                self.clear_console()
                choice = input("Select number of task (1 - 5)\n0 - Exit\n\nYour Choice: ")
                if choice in self.valid_choices:
                    self.handle_choice(choice)
                    input(f"\nTask {choice} completed! Press any button to continue..\n")
                elif choice == '0':
                    print("\nExit!\n")
                    return
                else:
                    self.clear_console()
                    print("Insert right number, redneck!")
        else:
            print("Wrong folder path!")


if __name__ == "__main__":
    main = Main()
    main.main_function()