Network Security Data Analysis

A machine learning-based project for analyzing network traffic and detecting potential security threats. The system processes raw network data, validates it against defined schemas, and uses trained models to predict anomalies or malicious activities.

🚀 Features

Data Ingestion: Load and validate network datasets (Network_Data, valid_data).

Schema Validation: Ensures consistent input formats via data_schema/.

Model Training & Deployment: Uses pre-trained models stored in final_model/.

Prediction Output: Generates threat analysis results stored in prediction_output/.

Web Interface: Simple UI (Flask templates) to visualize results.

Containerized Deployment: Docker support for easy setup and deployment.

🛠 Tech Stack

Language: Python 3

Libraries: (see requirements.txt) – likely includes Pandas, Scikit-learn, Flask, etc.

Deployment: Docker

⚙️ Installation

Clone the repository:

git clone https://github.com/samyak8505/Network_Security_DataAnalysis.git
cd Network_Security_DataAnalysis


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


▶️ Usage

Run Flask App:

python app.py


Access at http://localhost:5000


