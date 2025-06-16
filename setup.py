from setuptools import setup, find_packages

setup(
    name="agriculture-price-prediction",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'flask>=3.0.0',
        'gunicorn>=21.2.0',
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scikit-learn>=1.3.0',
        'xgboost>=2.0.3',
        'groq>=0.4.2',
        'python-dotenv>=0.19.0',
    ],
    python_requires='>=3.8',
)
