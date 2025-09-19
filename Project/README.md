# ForestFires
This project is a Flask web application that predicts the Fire Weather Index (FWI) using the Algerian Forest Fire dataset. The FWI is an important indicator of wildfire risk, influenced by weather conditions such as temperature, humidity, wind, and rainfall.

The application allows users to enter environmental factors (Temperature, RH, Wind Speed, Rain, FFMC, DMC, DC, ISI, Classes, and Region) through a simple HTML form. These inputs are preprocessed using a StandardScaler, and a trained Ridge Regression model generates the prediction.

The project demonstrates the complete ML pipeline:

Model training with scikit-learn

Model serialization using pickle

Flask integration for real-time prediction

Web interface for interactive user input

Features : --- 

Clean Flask interface with form-based input

Real-time FWI prediction

Pre-trained Ridge Regression model

User-friendly design with minimal dependencies

Tech Stack

Python, Flask

scikit-learn (Ridge Regression, StandardScaler)

HTML (Jinja2 templates)
