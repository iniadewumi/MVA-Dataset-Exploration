import requests, subprocess
import io, pathlib, zipfile, os
import pandas as pd
import numpy as np



def leaf_dataset():
    global wine, zoo, leaf

    link = "https://archive.ics.uci.edu/ml/machine-learning-databases/00288/leaf.zip"
    
    subprocess.run(["curl", f"{link}", "-o", f'/leaf'])
    
    
    
    BASE_DIR = pathlib.Path().resolve().parent / "MVA"
    DATASETS_DIR = BASE_DIR / "datasets"
    ZIPS_DIR = DATASETS_DIR / "zips"
    os.makedirs(ZIPS_DIR, exist_ok=True)
    
    
    def download_spam_collection(link, filename):
        if not os.path.exists(f'{ZIPS_DIR}/{filename}'):
            subprocess.run(["curl", f"{link}", "-o", f'{ZIPS_DIR}/{filename}'])
        else:
            print(f"File {filename} exist!")
    
    
    def unzip_spam_collection(filepath, destination):
        if len(os.listdir(destination))<1:
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(destination)
                return
        loc = str(destination).split('\\')[-1]
        print(f"Did not unzip because {loc} already contains files")
     
        
    download_spam_collection(link, "leaf.zip")
    destination=DATASETS_DIR/"leaf"
    unzip_spam_collection(filepath=ZIPS_DIR/"leaf.zip", destination=DATASETS_DIR/"leaf")
        
    leaf = pd.read_csv(destination/"leaf.csv")
        
    leaf_cor = pd.DataFrame(np.corrcoef(leaf))
    leaf_cov = pd.DataFrame(np.cov(leaf))
    
    def check():
        print("No NA:", leaf.dropna().shape == leaf.shape)
        print("Size:", leaf.shape)
        print("Cor:", leaf_cor)
        print("Cov:", leaf_cov)
        return 
    check()
    


print("\n\nLeaf")
leaf_dataset()
