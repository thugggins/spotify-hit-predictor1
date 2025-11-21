Spotify Hit Predictor (ML Demo Interface)

This repository contains a simple, interactive web interface demonstrating a machine learning model that predicts the popularity score of a Spotify track based on three key features: Artist Popularity, Track Duration, and Album Track Count.

Note: The application in index.html uses a simulated Linear Regression model with hardcoded weights and a small sample of tracks from the dataset for demonstration purposes.

🚀 Live Demo

This application is designed to be hosted on a static site provider (like GitHub Pages or Netlify).

To view the live demo: Simply upload this repository to GitHub and enable GitHub Pages on the main branch.

⚙️ Features

Simulated ML Prediction: Uses a simple Linear Regression formula with pre-defined weights to predict track popularity (0-100).

Dataset Integration: Loads sample tracks from a hardcoded list, enabling users to test real data points.

Read-Only Features: Key feature fields (Artist Popularity, Duration, Album Tracks) are locked when a dataset track is selected to prevent accidental modification of real data.

Manual Input Mode: Allows users to manually enter hypothetical feature values to test the model's response to custom scenarios.

📈 Included Python Analysis

This project also includes the initial Python scripts used for preparing and analyzing the data:

File Name

Description

data_loading.py

Loads and performs initial checks on the source spotify_data clean.csv file.

spotify_project_analysis.py

Performs Exploratory Data Analysis (EDA), prints summary statistics, and generates visualizations (e.g., popularity distribution, trend over time).

🛠️ Technology Stack

Frontend: HTML5, Tailwind CSS (via CDN), Vanilla JavaScript.

Backend (Simulated): Hardcoded Linear Regression function in JavaScript.

Data Analysis: Python (Pandas, NumPy, Matplotlib, Seaborn).