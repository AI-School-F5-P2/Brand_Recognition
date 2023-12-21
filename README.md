# Brand Recognition Tool

<div align="center">
[![Project Demo](https://img.youtube.com/vi/5EVDUKvmI_E/0.jpg)](https://youtu.be/5EVDUKvmI_E)
</div>

---

## Overview

Welcome to the Brand Detection Tool repository!
This computer vision project focuses on the detection of various commercial brands in videos. The goal is to develop an AI tool capable of identifying brands, extracting relevant information such as the label name, confidence percentage, duration on screen, and size.

The collected information is stored in a database, and a text file report is generated. This data is particularly useful in product placement campaigns to verify contractual conditions, conduct A/B tests, and assess the campaign's impact for further improvements.

---

## Dataset

We have curated a dataset with over 1000 manually selected and labeled images. Subsequently, we trained the YOLOv8 model using this dataset for 200 epochs.

---

## YOLOv8 Model

The YOLOv8 model demonstrates high precision in detecting brands in videos, even in varied positions, perspectives, or when the brand is partially visible, blurred, or in a small size. The model has been trained with our custom dataset, resulting in the 'best.pt' model file.

---

## Project Structure

* **main.py:** Execute this script to process a video using the retrained YOLOv8 model. It generates a new video with detections, a report named 'detections.txt,' and stores the data in the database.

* **model/:** Folder containing YOLOv8 model-related files.

    - **yolov8_training.ipynb:** Google Colab notebook used for training the YOLOv8 model with our custom dataset.

    - **best.pt:** YOLOv8 model trained with our data and optimized weights.

    - **predict_video.py:** is a Python script designed as an alternative to `main.py` for scenarios where database interaction is not required. This script processes a specified video using the retrained YOLOv8 model, generating a new video with brand detections and a detailed report ('detections.txt'). It proves particularly useful for conducting tests and experiments without the need for database operations.

* **database/:** Folder containing database-related scripts.
    - **database.py:** Script for managing the database.
    - **brands_logos.sql:** SQL file with the database table structure.

---

## Getting Started

**1. Clone the Repository:** Begin by cloning this repository to your local machine:

```bash
https://github.com/PalomaGGC/Brand_Recognition.git
cd Brand_Recognition
```

**2. Install Dependencies:** Ensure you have the necessary dependencies installed by running:

```bash
pip install -r requirements.txt
```

**3. Create a Videos Folder:** Create a folder named "videos" and place the videos you want to process inside it. Currently, the tool detects Coca-Cola, HBO, and Renault.

**4. Run the Tool:**  Execute main.py to process the videos, saving the results in the database, or run predict_video.py to process the videos without using the database.

**5. Explore Results:** Check the generated video, report (detections.txt), and database entries for valuable insights.

Feel free to reach out if you have any questions or suggestions! Happy brand detecting!
