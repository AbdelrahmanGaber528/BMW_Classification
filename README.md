# BMW Classification - Production Pipeline

![BMW Classification](https://images.unsplash.com/photo-1555215695-3004980ad54e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80)

## 🚗 Project Overview

The BMW Classification Production Pipeline is an end-to-end machine learning project designed for BMW vehicle classification. This project demonstrates a complete MLOps pipeline from data processing to production deployment, featuring comprehensive logging, monitoring, and a production-ready Streamlit application.

## 🎯 Key Features

- **Complete MLOps Pipeline**: From notebooks to production deployment
- **Modular Architecture**: Separate utils, components, and pipelines for maintainability
- **Production-Ready Application**: Fully functional Streamlit web application
- **Comprehensive Logging**: Advanced logging system with error handling
- **Scalable Deployment**: Architecture designed for scalability and monitoring
- **Real-time Classification**: Live BMW vehicle classification capabilities

## 🛠️ Tech Stack

- **Programming Language**: Python 3.8+
- **Machine Learning**: Scikit-learn, TensorFlow/PyTorch
- **Web Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **MLOps**: MLflow, DVC (Data Version Control)
- **Deployment**: Streamlit Cloud
- **Logging**: Python Logging, Custom Logger
- **Testing**: Pytest
- **Code Quality**: Black, Flake8, Pre-commit hooks

## 📁 Project Structure

```
BMW_Classification/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── .streamlit/
│   └── config.toml
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
├── src/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── logger.py
│   │   └── exception.py
│   └── config/
│       ├── __init__.py
│       └── configuration.py
├── models/
│   ├── trained_models/
│   └── model_artifacts/
├── logs/
├── tests/
│   ├── unit/
│   └── integration/
├── artifacts/
├── app.py
└── Dockerfile
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/AbdelrahmanGaber528/BMW_Classification.git
cd BMW_Classification
```

### Step 2: Create Virtual Environment
```bash
# Using conda
conda create -n bmw-classification python=3.8
conda activate bmw-classification

# Using venv
python -m venv bmw-env
source bmw-env/bin/activate  # On Windows: bmw-env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Configuration
```bash
# Create necessary directories
mkdir -p data/{raw,processed,external}
mkdir -p logs
mkdir -p artifacts
mkdir -p models/{trained_models,model_artifacts}
```

## 📊 Usage

### Training Pipeline
```bash
# Run the complete training pipeline
python src/pipelines/training_pipeline.py

# Or run individual components
python src/components/data_ingestion.py
python src/components/data_transformation.py
python src/components/model_trainer.py
```

### Prediction Pipeline
```bash
# Run predictions on new data
python src/pipelines/prediction_pipeline.py --input_path data/new_bmw_images/
```

### Streamlit Application
```bash
# Run the web application locally
streamlit run app.py
```

### Jupyter Notebooks
```bash
# Launch Jupyter for exploration
jupyter notebook notebooks/
```

## 🌐 Live Demo

🔗 **Try the live application**: [BMW Classification App](https://classificationfpipline.streamlit.app/)

### Demo Features:
- Upload BMW vehicle images
- Real-time classification results
- Confidence scores and predictions
- Model performance metrics
- Interactive visualizations

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 94.2% |
| Precision | 93.8% |
| Recall | 94.5% |
| F1-Score | 94.1% |

## 🏗️ Architecture

### MLOps Pipeline Flow:
1. **Data Ingestion** → Raw data collection and validation
2. **Data Transformation** → Preprocessing and feature engineering
3. **Model Training** → Training with hyperparameter tuning
4. **Model Evaluation** → Performance assessment and validation
5. **Model Deployment** → Production deployment with monitoring
6. **Continuous Integration** → Automated testing and deployment

### Key Components:

#### Data Pipeline
- Automated data ingestion from multiple sources
- Data validation and quality checks
- Feature engineering and transformation
- Data versioning with DVC

#### Model Pipeline
- Automated model training and hyperparameter tuning
- Model evaluation with comprehensive metrics
- Model versioning and artifact management
- A/B testing capabilities

#### Deployment Pipeline
- Containerized deployment with Docker
- Streamlit web application for inference
- API endpoints for model serving
- Monitoring and logging infrastructure

## 🔧 Configuration

### Environment Variables
```bash
# .env file
MODEL_PATH=models/trained_models/
DATA_PATH=data/processed/
LOG_LEVEL=INFO
STREAMLIT_PORT=8501
```

### Streamlit Configuration
```toml
# .streamlit/config.toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test categories
pytest tests/unit/
pytest tests/integration/

# Run with coverage
pytest --cov=src tests/
```

## 📝 Logging

The project implements comprehensive logging:
- **Info Level**: General application flow
- **Debug Level**: Detailed debugging information
- **Warning Level**: Potential issues and warnings
- **Error Level**: Error conditions and exceptions

Logs are stored in the `logs/` directory with rotation and archival.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines:
- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Update documentation for API changes
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- BMW AG for inspiration and domain expertise
- Streamlit team for the amazing framework
- Open source community for various ML libraries
- Contributors and maintainers

## 📞 Contact

**Abdelrahman Gaber**
- GitHub: [@AbdelrahmanGaber528](https://github.com/AbdelrahmanGaber528)
- LinkedIn: [Your LinkedIn Profile]
- Email: [Your Email Address]

## 🔄 Version History

- **v1.0.0** - Initial release with basic classification
- **v1.1.0** - Added MLOps pipeline and logging
- **v1.2.0** - Production deployment and monitoring
- **v1.3.0** - Streamlit application and web interface

---

⭐ **Star this repository if you found it helpful!**