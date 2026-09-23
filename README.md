# FastAPI Machine Learning API: Insurance Premium Predictor

![Python](https://img.shields.io/badge/Python-3.11-007acc?logo=python&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Pipeline-e67e22?logo=scikit-learn&logoColor=white) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Advanced-27ae60) ![Pydantic](https://img.shields.io/badge/Pydantic-Validation-000000?logo=pydantic&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-API-1abc9c?logo=fastapi&logoColor=white)


This project serves as a practical implementation to track my learning journey of integrating Machine Learning models into production-ready web APIs. It exposes a Scikit-Learn Random Forest model via **FastAPI**, featuring robust input validation and automated feature engineering using **Pydantic**.

The API predicts a user's **Insurance Premium Category** (`Low`, `Medium`, or `High`) based on their demographic details, lifestyle habits, and occupation.

## ✨ Features

* **End-to-End ML Integration**: Seamlessly serves a pre-trained `scikit-learn` Random Forest model through a RESTful API.
* **Automated Feature Engineering**: Utilizes Pydantic `@computed_field` decorators to automatically derive complex features (BMI, Age Group, Lifestyle Risk, and City Tier) from raw user input on the fly.
* **Strict Input Validation**: Leverages Pydantic to ensure all incoming data is type-checked, range-bound, and sanitized before reaching the model.
* **Confidence Scoring**: Returns not just the predicted category, but also the model's confidence score and the probability distribution across all possible classes.
* **Health Monitoring**: Includes a dedicated health check endpoint to monitor API status and model availability.

## 🛠️ Tech Stack

* **Web Framework:** [FastAPI](https://fastapi.tiangolo.com/) - For building high-performance APIs.
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/) - For request/response schemas and derived calculations.
* **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) - For the Random Forest Classifier pipeline (Data preprocessing + inference).
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/) - For DataFrame handling during model inference.
* **Server:** [Uvicorn](https://www.uvicorn.org/) - ASGI web server.

## 📂 Project Structure

```text
.
├── app.py                           # Main FastAPI application and route definitions
├── config/
│   └── city_tier.py                 # Configuration lists for Tier 1 and Tier 2 cities
├── model/
│   ├── ml_train/
│   │   ├── insurance.csv            # Original training dataset
│   │   └── train_ml.ipynb           # Jupyter notebook containing EDA and model training
│   ├── model.pkl                    # Pickled Scikit-Learn pipeline (Preprocessing + Model)
│   └── predict.py                   # Inference logic and model loading
├── schema/
│   ├── prediction_reponse.py        # Pydantic schema for the API response
│   └── user_input_validation.py     # Pydantic schema for input validation and feature creation
├── pyproject.toml                   # Project dependencies and metadata
└── README.md                        # Project documentation
```

## ⚙️ Setup and Installation

### Prerequisites
* Python 3.11 or higher
* [uv](https://github.com/astral-sh/uv) (recommended) or standard `pip` for dependency management.

### Installation Steps

1. **Clone the repository (if applicable):**
   ```bash
   git clone <your-repo-url>
   cd ml-through-fastapi
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   Since the project uses `pyproject.toml`, you can install it directly:
   ```bash
   pip install -e .
   ```
   *(Note: The dependencies include `fastapi`, `pandas`, `pydantic`, `scikit-learn`, and `uvicorn`)*.

## 🚀 How to Run It

Start the FastAPI application using Uvicorn with live-reload enabled:

```bash
uvicorn app:app --reload
```

The API will start running locally at: `http://127.0.0.1:8000`

You can immediately explore and test the API using FastAPI's built-in interactive documentation:
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

## 📡 API Endpoints

### 1. Root / Home
* **Endpoint:** `GET /`
* **Description:** Simple welcome message to verify the server is running.
* **Response:**
  ```json
  {
    "message": "This is the home page of this API"
  }
  ```

### 2. Health Check
* **Endpoint:** `GET /health`
* **Description:** Checks the health of the API and verifies if the ML model (`model.pkl`) was loaded successfully into memory.
* **Response:**
  ```json
  {
    "status": "OK",
    "version": "1.0.0",
    "model_loaded": true
  }
  ```

### 3. Predict Premium Category
* **Endpoint:** `POST /predict`
* **Description:** Accepts user data, performs validation and dynamic feature engineering, and returns the predicted insurance premium category.

**Request Body (JSON):**
```json
{
  "age": 28,
  "weight": 75.5,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response (JSON):**
*(Note: The JSON response structure reflects the Pydantic schema definitions)*
```json
{
  "response": {
    "predicted_category": "Low",
    "confidence": 0.85,
    "class_probabalities": {
      "Low": 0.85,
      "Medium": 0.12,
      "High": 0.03
    }
  }
}
```

## 🧠 Behind the Scenes: Model & Data

* **Training Data:** The model was trained on a synthetic dataset (`insurance.csv`) containing records of age, weight, height, income, smoking habits, city, and occupation.
* **Feature Engineering Pipeline:** 
  Raw inputs are transformed by Pydantic properties:
  * `bmi` is calculated from `weight` and `height`.
  * `age_group` is categorized into young, adult, middle_age, or senior.
  * `lifestyle_risk` is determined by a combination of smoking status and BMI.
  * `city_tier` evaluates if the city falls into Tier 1, Tier 2, or Tier 3 lists.
* **The Model:** A `RandomForestClassifier` packaged within a `Pipeline` that includes a `ColumnTransformer` (handling One-Hot Encoding for categorical variables).

---
*Built with ❤️ to learn Machine Learning & API Integration.*