# SaferoadAI

SaferoadAI is a real-time car accident detection system that utilizes a YOLO model trained on a custom dataset. The system is designed to work with a video feed from **CCTV or live stream**, detecting accidents in real-time and sending messages to the nearest hospital using the **OLA Maps API**.

## Features
- **Real-time accident detection** using YOLOv8.
- **Custom-trained model** on a car accident dataset.
- **Integration with CCTV or live video feeds** for practical applications.
- **Automatic alert system** using OLA Maps API to notify the nearest hospital.
- **Frame capture and image conversion** to URL for message attachments.
- **Potential for further enhancements**, such as traffic control automation.

## Installation

### Prerequisites
Ensure you have the following installed before proceeding:
- Python 3.8+
- PyTorch
- Ultralytics YOLOv8
- OpenCV
- Streamlit (for deployment, if needed)
- OLA Maps API access

### Clone the Repository
```bash
git clone https://github.com/aayush010904/SaferoadAI.git
cd SaferoadAI
```

### Install Dependencies
```bash
pip install -r requirements.txt
```
### Datset 
Dataset used for training : [Roboflow datset URL](https://universe.roboflow.com/accident-detection-model/accident-detection-model/dataset/2)
## Usage

### Running the Application
To start the accident detection system, run:
```bash
python app.py
```

### How It Works
- `app.py` imports functions from `SendMessage.py` and `NearestHospital.py` to send messages and fetch the nearest hospital.
- When an accident is detected, the frame is saved.
- The saved frame is converted into a URL using `Image2Url.py`.
- The image URL is sent along with an alert message to the nearest hospital.

### Training the YOLOv8 Model (If Needed)
```bash
python model_training.ipynb
```

## Deployment
The model can be deployed using Streamlit:
```bash
streamlit run app.py
```

## Project Structure
```
SaferoadAI/
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables
├── best.pt               # Pre-trained YOLO model
├── best_model.pt         # Additional trained model
├── model_training.ipynb  # YOLO model training notebook
├── Image2Url.py          # Converts detected accident frames to image URLs
├── NearestHospital.py    # Fetches nearest hospital using OLA Maps API
├── SendMessage.py        # Sends alert messages with accident details
├── currentLocation.py    # Determines the user's current location
└── other_files/          # Additional scripts or resources
```

## Future Enhancements
- Improving model accuracy with more training data.
- Expanding API support for other mapping services.
- Implementing real-time traffic management integration.

## Contributions
Feel free to open an issue or submit a pull request if you’d like to contribute!

## License
This project is licensed under the MIT License.

## Author(s)
**Aayush Chauhan**  
📧 Contact: [aayushchauhan019@gmail.com](mailto:aayushchauhan019@gmail.com)  
🔗 LinkedIn: [Aayush Chauhan](www.linkedin.com/in/aayushchauhan019)

**Manish Sharma**

📧 Contact: [manishshar@gmail.com](mailto:manishshar39@gmail.com)  
🔗 LinkedIn: [Manish Sharma](https://www.linkedin.com/in/manishsharmadu/)

**Ekansh Dubey**

📧 Contact: [ekanshdubey@ee.du.ac.in](mailto:ekanshdubey@ee.du.ac.in)  
🔗 LinkedIn: [Ekansh Dubey](www.linkedin.com/in/ekansh-dubey-0b2808227/)
