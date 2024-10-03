class Task3Manager:

    @staticmethod
    def separate_images_into_sets(folder_images):

        learning_subset = []
        validate_subset = []
        control_subset = []

        folders_count = len(folder_images)

        count_of_learning_images_to_append_per_folder = int(200000 / folders_count)
        count_of_validate_images_to_append_per_folder = int(10000 / folders_count)
        count_of_control_images_to_append_per_folder = int(19000 / folders_count)

        for folder in folder_images:
                learning_subset += folder['images'][:count_of_learning_images_to_append_per_folder]
                validate_subset += folder['images'][count_of_learning_images_to_append_per_folder:(count_of_learning_images_to_append_per_folder + count_of_validate_images_to_append_per_folder)]
                control_subset += folder['images'][(count_of_learning_images_to_append_per_folder + count_of_validate_images_to_append_per_folder):(count_of_learning_images_to_append_per_folder + count_of_validate_images_to_append_per_folder + count_of_control_images_to_append_per_folder)]

        print("Successfully separated into sets!\n")
        print(f"Learning Set count: {len(learning_subset)}")
        print(f"Validate Set count: {len(validate_subset)}")
        print(f"Control Set count: {len(control_subset)}")

        return learning_subset, validate_subset, control_subset