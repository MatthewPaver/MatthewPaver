# Welcome to the Architexa Repository!

This README provides a comprehensive overview of the various folders within the project directory, detailing their contents and purposes.

## Folder Structure and Descriptions

### Legacy Code
- **Description**: Houses all old versions of scripts and codebases previously used or considered during the development process.
- **Purpose**: Serves as a historical archive and backup. These files are not required for the project's operation.

### Dataset
- **Description**: This folder is central to the project's data handling. It includes:
  - Scripts for dataset creation.
  - The complete dataset used for model training and testing.
  - An unaugmented version of the dataset.
- **Purpose**: Essential for users looking to understand or recreate the dataset used in model training.

### Test Trained Model
- **Description**: Contains a script (`test_model.py`) to run the trained model and generate an output image (`test.png`).
  - **Variable**: `class_number` (range 1-5) can be modified to produce different types of images based on the class.
- **Purpose**: To demonstrate and test the functionality of the trained model using predefined classes.

### Neural Network Code
- **Description**: Includes all scripts related to the neural network's architecture, including building, training, and tuning the model.
  - **Key Script**: `worker.py` - Runs the training script. Contains a dummy trial to ensure the script operates correctly without stored trials from a cloud broker.
- **Purpose**: Crucial for users interested in the technical details of the neural network or who wish to run training processes independently.

## Usage Instructions

Each folder is structured to provide clarity and ease of access to the project's resources. Users are encouraged to explore the `Dataset` folder for data-related scripts and the `Neural Network Code` folder to engage with the model's training and testing scripts. Adjustments to scripts such as `test_model.py` should be made carefully to ensure accurate outputs.

For further details on running specific scripts or setting up the environment, refer to the individual README files within each folder or contact the project maintainers.
This respository can be found [Here](https://github.com/MatthewPaver/208-Project)

