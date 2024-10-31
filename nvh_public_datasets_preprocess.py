# Import necessary libraries
import pandas as pd
import os

# Step 1: Load the datasets
# Setting up paths for GitHub Codespace compatibility
BASE_DIR = os.getenv('GITHUB_WORKSPACE', '.')

# Car Evaluation Dataset - Load from UCI Repository and Add Headers
# Dataset Link: https://archive.ics.uci.edu/ml/datasets/Car+Evaluation
car_eval_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
car_eval_columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
car_eval_csv_path = os.path.join(BASE_DIR, 'car_evaluation_with_headers.csv')

# Downloading and Saving the Car Evaluation dataset if not already present
if not os.path.exists(car_eval_csv_path):
    car_eval_df = pd.read_csv(car_eval_url, header=None, names=car_eval_columns)
    car_eval_df.to_csv(car_eval_csv_path, index=False)
filtered_car_eval_df = pd.read_csv(car_eval_csv_path)

# Vehicle Silhouettes Dataset - Load from UCI Repository and Add Headers
# Dataset Link: https://archive.ics.uci.edu/ml/datasets/Automobile
vehicle_silhouettes_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
vehicle_silhouettes_columns = ['symboling', 'normalized_losses', 'make', 'fuel_type', 'aspiration', 'num_of_doors', 'body_style', 'drive_wheels', 'engine_location', 'wheel_base', 'length', 'width', 'height', 'curb_weight', 'engine_type', 'num_of_cylinders', 'engine_size', 'fuel_system', 'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm', 'city_mpg', 'highway_mpg', 'price']
vehicle_silhouettes_csv_path = os.path.join(BASE_DIR, 'vehicle_silhouettes_with_headers.csv')

# Downloading and Saving the Vehicle Silhouettes dataset if not already present
if not os.path.exists(vehicle_silhouettes_csv_path):
    vehicle_silhouettes_df = pd.read_csv(vehicle_silhouettes_url, header=None, names=vehicle_silhouettes_columns, na_values='?')
    vehicle_silhouettes_df.to_csv(vehicle_silhouettes_csv_path, index=False)
filtered_vehicle_silhouettes_df = pd.read_csv(vehicle_silhouettes_csv_path)
