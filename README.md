# Autolock: System Security with Facial Recognition


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

Autolock is a Python-based system utility designed to enhance security through facial recognition technology. It automatically locks the system when an unauthorized user is detected, making it suitable for cybersecurity applications. Leveraging computer vision techniques, Autolock offers advanced authentication features while ensuring user privacy. By combining face detection and recognition algorithms with input blocking mechanisms, Autolock provides a seamless and secure access control solution for protecting sensitive data and preventing unauthorized access. Autolock is an open-source project that can be customized and extended to meet specific security requirements, making it a valuable tool for cybersecurity professionals, researchers, and developers seeking to enhance system security with facial recognition technology.

## Features

Autolock offers the following features to enhance system security with facial recognition technology:

- **Facial Recognition:** Utilizes state-of-the-art face recognition algorithms to authenticate users based on their facial features, ensuring secure access control.
- **Face Detection:** Detects faces in real-time using the webcam, enabling seamless and efficient user authentication without the need for manual input.
- **User Authentication:** Compares captured faces with a database of known faces to authenticate users, providing a seamless and secure login experience.
- **Privacy Protection:** Ensures user privacy by securely storing face data and implementing robust encryption mechanisms to protect sensitive information.
- **Input Blocking:** Disables keyboard and mouse input when an unauthorized user is detected, preventing unauthorized access and ensuring system integrity.
- **Automatic Locking:** Automatically locks the system when an unauthorized user is detected, enhancing security and protecting sensitive data from unauthorized access.
- **Customizable Settings:** Offers configurable settings for face recognition parameters, input blocking mechanisms, and user authentication methods, allowing users to customize the authentication process according to their security requirements.
- **Threshold Adjustment:** Allows users to adjust the face recognition threshold to control the sensitivity of the authentication process, ensuring accurate identification while minimizing false positives.
- **GUI Interface:** Provides a user-friendly graphical interface for easy configuration and management, making it suitable for both novice and advanced users.

## Requirements

- **Python 3.x**
- **OpenCV (`opencv-python`):** Open-source computer vision library for image and video processing.
- **NumPy (`numpy`):** Fundamental package for scientific computing with Python.
- **Face Recognition (`face_recognition`):** Library for face recognition built on top of dlib and OpenCV.
- **Tkinter (optional):** GUI toolkit for Python, used for creating the graphical interface.

## Installation

1. **Clone the Repository:**
   
    ```
    git clone https://github.com/yourusername/Autolock.git
    ```

2. **Install Dependencies:**
   
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Populate the `face` Directory:**
   
    Add images of authorized users to the `face` directory to create a database of known faces.

2. **Run the `main.py` Script:**
   
    ```
    python main.py
    ```

3. **Authenticate Users:**
   
    Autolock will use the webcam to capture faces and compare them with the database of known faces. If an unauthorized user is detected, the system will automatically lock to prevent access.

## Customization

- **Threshold Adjustment:** Modify the face recognition threshold in the `face_confidence()` function to customize the sensitivity of the authentication process according to your security requirements.
- **GUI Customization:** Customize the graphical interface to match your organization's branding and design preferences.

## Contribution Guidelines

Contributions to Autolock are welcome! If you have ideas for new features, improvements, or bug fixes, please submit a pull request.

## License

Autolock is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Face Recognition Library:** [https://github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)
- **OpenCV:** [https://github.com/opencv/opencv](https://github.com/opencv/opencv)
ew of Autolock, highlighting its features, installation instructions, usage guidelines, and customization options, with a focus on its relevance to cybersecurity and computer vision professionals.