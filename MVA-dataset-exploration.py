import requests, subprocess
import io, pathlib, zipfile, os
import pandas as pd
import numpy as np

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00288/leaf.zip"
# url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.names"

# data = requests.get(url).text
# df = pd.read_csv(io.StringIO(data))

# head = requests.get(url2).text



# import zipfile

# filepath = "C:\\Users\\adewu\\Downloads\\GPS Trajectory.rar"


# requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/00354/GPS%20Trajectory.rar").text


global wine, zoo, leaf
# def zoo_dataset():
#     global wine, zoo, leaf
#     url="https://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data"
    
#     data = requests.get(url).text
#     zoo = pd.read_csv(io.StringIO(data))
#     zoo_cor = pd.DataFrame(np.corrcoef(zoo[zoo.columns[1:]]))
#     zoo_cov = pd.DataFrame(np.cov(zoo[zoo.columns[1:]]))
    
#     def check():
#         print("No NA:", zoo.dropna().shape == zoo.shape)
#         print("Size:", zoo.shape)
#         print("Cor:", zoo_cor)
#         print("Cov:", zoo_cov)
#         return 
#     check()

# def wine_dataset():
#     global wine, zoo, leaf

#     url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    
#     data = requests.get(url).text
#     wine = pd.read_csv(io.StringIO(data))
#     wine_cor = pd.DataFrame(np.corrcoef(wine))
#     wine_cov = pd.DataFrame(np.cov(wine))
    
#     def check():
#         print("No NA:", wine.dropna().shape == wine.shape)
#         print("Size:", wine.shape)
#         print("Cor:", wine_cor)
#         print("Cov:", wine_cov)
#         return 
#     check()



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
    
    
    
    destination=DATASETS_DIR/"movies"
    os.makedirs(destination, exist_ok=True)
    unzip_spam_collection(filepath="C:\\Users\\adewu\\Downloads\\archive.zip", destination=DATASETS_DIR/"movies")
    
    
    
    os.listdir(destination)
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