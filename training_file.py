import pandas as pd
import glob

files = glob.glob("*.HEIC") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.JPG")
print(len(files))  # Check how many data

df = pd.DataFrame(files)
df.columns = ['filename']

df.to_excel('test.xlsx')
