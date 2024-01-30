# How to mount Google Drive to a Google Colab notebook

To mount Google Drive to a Google Colab notebook and access a CSV file dataset from Google Drive, you can follow these steps:

## Step 1:

Open a new or existing Google Colab notebook.

## Step 2:

Mount your Google Drive to the notebook by running the following code snippet and following the prompts:

```python
from google.colab import drive
drive.mount('/content/drive')
```

## Step 3:

Once you have mounted your Google Drive, navigate to the CSV file dataset that you want to use in the file explorer. You can do this by clicking on the "Files" tab in the left-hand panel of the notebook and navigating to the appropriate folder.

## Step 4: 

Copy the path to the CSV file dataset by right-clicking on the file and selecting "Copy path".

## Step 5: 

Use the path to the CSV file dataset to read the data into a Pandas DataFrame. For example:

```python
import pandas as pd

# replace with the path to your CSV file
file_path = '/content/drive/MyDrive/path/to/your/dataset.csv'

# read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# display the first 5 rows of the DataFrame
print(df.head())
```

That's it! You should now be able to access your CSV file dataset from Google Drive and start working with it in your Google Colab notebook.
