# oko-cv
A PoC Computer Vision Python Application Helping Visually Impaired People

This project aims to develop a proof-of-concept (PoC) application leveraging computer vision to assist visually impaired individuals. 
The application utilizes advanced techniques in image processing and machine learning to provide real-time assistance through features such as:

- Object Detection: Identifies and labels objects in the user's environment.
- Text Recognition: Converts text from images into speech, enabling users to read printed materials.
- Scene Understanding: Provides contextual information about the surroundings.
- Audio Feedback: Delivers information audibly to the user, ensuring accessibility.


The goal of this project is to enhance the independence and quality of life for visually impaired individuals by offering a reliable and user-friendly tool that can be used in various everyday scenarios.

### Software used
- [Python](https://www.python.org)
- [OpenCV](https://opencv.org)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) with YOLO11 model
- [llava model](https://ollama.com/library/llava)

### Setup
- Install Python 3.12.x
- Clone the repository
- Install ollama server
- Pull the LLAVA model by running `ollama run llava:7b`
- Install the dependencies by running `pip install -r requirements.txt`
