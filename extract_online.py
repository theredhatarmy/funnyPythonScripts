# Import necessary libraries
import os
import tarfile
import urllib.request

# Define the URL and data directory
url = "http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"
data_dir = "/content/food-101/images"  # Path where the images will be stored

# Download the dataset
dataset_path = "/content/food-101.tar.gz"
urllib.request.urlretrieve(url, dataset_path)

# Extract the tar.gz file
with tarfile.open(dataset_path, "r:gz") as tar:
    tar.extractall(path="/content/food-101")

# Verify if the data is extracted properly
os.listdir("/content/food-101")
