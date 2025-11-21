import pandas as pd
import numpy as np
from IPython.display import display

# Define the file path for the uploaded dataset
FILE_PATH = "spotify_data clean.csv"

# --- Step 1: Data Loading ---
print("--- Step 1: Loading Data ---")
try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(FILE_PATH)
    print(f"Data loaded successfully from: {FILE_PATH}")

    # --- Step 2: Data Confirmation (Head) ---
    print("\n--- Step 2: First 5 Rows of the Dataset ---")
    display(df.head())

    # --- Step 3: Data Confirmation (Structure and Types) ---
    print("\n--- Step 3: Column Information (Types, Non-Null Counts) ---")
    df.info()

    # Specifically checking the 'explicit' column as requested for filtering
    print("\n--- Step 4: 'explicit' Column Value Counts ---")
    explicit_counts = df['explicit'].value_counts()
    print("Value Counts for 'explicit' column:")
    print(explicit_counts)
    print(f"\nData type of 'explicit' column: {df['explicit'].dtype}")


except FileNotFoundError:
    print(f"ERROR: The file '{FILE_PATH}' was not found.")
    print("Please ensure the file name is correct and accessible.")
except Exception as e:
    print(f"An error occurred during file processing: {e}")

# Save the DataFrame to a global variable for subsequent steps
# Note: In a real environment, you would typically pass the DataFrame between functions.
# For this interactive walkthrough, we'll assume 'df' is available for the next steps.
# In the next step, we will proceed with EDA.