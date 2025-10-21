# Traffic Sign Classification for Indian Road Conditions

## Overview
This project provides a robust solution for classifying traffic signs specific to Indian road conditions. Using a custom dataset and the YOLOv5 model, it delivers high-performance detection and classification capabilities. The system is integrated with Gradio for a user-friendly interface and supports multiple input formats, including images, videos, and real-time streams.

## Repository
This project is hosted on GitHub: [Traffic Sign Classification Repository](https://github.com/Karri001/Traffic-sign-classification)

## Features
- **Custom Dataset**: Trained on a specialized dataset tailored for Indian traffic signs to ensure accurate detection in diverse environments.
- **YOLOv5 Model**: Utilizes the power of YOLOv5 for efficient and accurate object detection.
- **Versatile Input Options**:
  - Static images
  - Video files
  - Real-time classification via webcam or external camera feeds
- **Gradio Interface**: Provides an intuitive, web-based interface for easy interaction with the model.

## How It Works
The system detects and classifies traffic signs in input media by leveraging the YOLOv5 architecture. The workflow includes:
1. **Data Preprocessing**: The custom dataset is preprocessed to ensure compatibility with YOLOv5 training requirements.
2. **Model Training**: The YOLOv5 model is fine-tuned using the custom dataset to optimize for Indian traffic signs.
3. **Inference**: Supports inference on:
   - Single images
   - Video streams (offline and real-time)
4. **Visualization**: Highlights detected traffic signs with bounding boxes and class labels.

## Setup and Installation
Follow these steps to set up the project:

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Karri001/Traffic-sign-classification.git
   cd Traffic-sign-classification
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the trained model weights:
   - Place the YOLOv5 model weights (`best.pt`) in the `models/` directory.

### Run the Application
Start the Gradio interface:
```bash
python app.py
```
The Gradio interface will launch, and you can access it via the displayed URL.

## Usage
### Using the Gradio Interface
1. **Upload an Image or Video**: Drag and drop a file into the provided input box.
2. **Real-Time Classification**: Select the webcam option to perform live traffic sign detection.
3. **View Results**: Detected traffic signs will be displayed with bounding boxes and class labels.

### Command-Line Interface (Optional)
For advanced users, inference can also be performed via the command line:
```bash
python detect.py --source <path_to_input> --weights models/best.pt
```

## Screenshots
### Gradio Interface
![Gradio Interface](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(279).png)


### Detection Result
![Detection Result](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(281).png)
![Detection Result](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(282).png)
![Detection Result](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(283).png)

### Video Demonstration
![Video Demonstration](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/video/WIN_20241130_00_07_38_Pro.mp4)

## Custom Dataset
The model is trained on a custom dataset that includes diverse traffic signs observed in Indian road conditions. The dataset contains:
- **Traffic Sign Types**: Speed limits, warning signs, mandatory signs, and more.
- **Environmental Variations**: Urban, rural, day, and night scenarios.

## Real-Time Performance
This system supports real-time traffic sign detection with minimal latency, making it suitable for applications such as:
- Autonomous vehicles
- Traffic monitoring systems
- Driver assistance tools

## Future Enhancements
- Adding more traffic sign classes for enhanced coverage.
- Improving performance for extreme weather and lighting conditions.
- Extending support for other road conditions beyond Indian scenarios.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is licensed under the [MIT License](LICENSE).

---

**Author**: K.Sai Sri Venkata Reddy

For questions or suggestions, please contact: [venkatreddykarri001@gmail.com.com]

