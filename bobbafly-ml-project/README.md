# BabbaFly ML Project

## Overview
This project predicts product prices using Machine Learning.

## Models Used
- Linear Regression
- Random Forest (Best Model)

## Results
- R² Score: 0.99
##Visualization
###Actual vs predicted graph


## API
POST /predict

Input:
{
  "brand": 1,
  "category": 0,
  "rating": 4
}

Output:
{
  "predicted_price": 2496
}

## Run
pip install -r requirements.txt  
python app.py
