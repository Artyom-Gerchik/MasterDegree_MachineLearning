import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class Task5Manager:
     
    @staticmethod
    def get_data_from_images(image_list):
        data = []
        labels = []
        for img_path in image_list:
            try:
                img = Image.open(img_path)
                img_array = np.array(img).flatten()
                data.append(img_array)

                label = os.path.basename(os.path.dirname(img_path))
                labels.append(label)
                print(f"Counter: {len(labels)}")
            except:
                print("Image cannot be processed")

        return np.array(data), np.array(labels)
    
    @staticmethod
    def learn_model_and_check_results(
        cls,
        learning_data,
        learning_labels,
        control_data,
        control_labels
    ):
        set_sizes = [50, 100, 1000, 50000]

        accuracies_50 = cls.learn_model(
            learning_data,
            learning_labels,
            control_data,
            control_labels,
            set_sizes,
            50
        )

        accuracies_100 = cls.learn_model(
            learning_data,
            learning_labels,
            control_data,
            control_labels,
            set_sizes,
            100
        )

        accuracies_1000 = cls.learn_model(
            learning_data,
            learning_labels,
            control_data,
            control_labels,
            set_sizes,
            1000
        )

        # accuracies_3000 = cls.learn_model(
        #     learning_data,
        #     learning_labels,
        #     control_data,
        #     control_labels,
        #     set_sizes,
        #     3000
        # )

        # accuracies_5000 = cls.learn_model(
        #     learning_data,
        #     learning_labels,
        #     control_data,
        #     control_labels,
        #     set_sizes,
        #     5000
        # )

        # accuracies_15000 = cls.learn_model(
        #     learning_data,
        #     learning_labels,
        #     control_data,
        #     control_labels,
        #     set_sizes,
        #     15000
        # )

        # accuracies_30000 = cls.learn_model(
        #     learning_data,
        #     learning_labels,
        #     control_data,
        #     control_labels,
        #     set_sizes,
        #     30000
        # )

        accuracies_50000 = cls.learn_model(
            learning_data,
            learning_labels,
            control_data,
            control_labels,
            set_sizes,
            50000
        )
        
        # Построение графика
        plt.plot(set_sizes, accuracies_50, marker='o', label='50 iterations')
        plt.plot(set_sizes, accuracies_100, marker='o', label='100 iterations')
        plt.plot(set_sizes, accuracies_1000, marker='o', label='1000 iterations')
        # plt.plot(set_sizes, accuracies_3000, marker='o', label='3000 iterations')
        # plt.plot(set_sizes, accuracies_5000, marker='o', label='5000 iterations')
        # plt.plot(set_sizes, accuracies_15000, marker='o', label='15000 iterations')
        # plt.plot(set_sizes, accuracies_30000, marker='o', label='30000 iterations')
        plt.plot(set_sizes, accuracies_50000, marker='o', label='50000 iterations')
        plt.xlabel('Training set size')
        plt.ylabel('Accuracy')
        plt.title('Dependence of classifier accuracy on training set size')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    @classmethod
    def learn_model(
        cls,
        learning_data,
        learning_labels,
        control_data,
        control_labels,
        sample_sizes,
        iterations
    ):
        accuracies = []
        for size in sample_sizes:
            X_sample, _, y_sample, _ = train_test_split(
                learning_data,
                learning_labels,
                train_size=size,
                random_state=42
            )
            
            model = LogisticRegression(max_iter=iterations)
            model.fit(X_sample, y_sample)
            
            y_pred = model.predict(control_data)
            accuracy = accuracy_score(control_labels, y_pred)
            accuracies.append(accuracy)

        print(f"\nModel learning on {iterations} iterations completed!\n")
        return accuracies