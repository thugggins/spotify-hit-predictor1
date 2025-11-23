import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuration ---
FILE_PATH = 'spotify_data clean.csv' # Assumes the file is in the same directory as the script
PLOT_STYLE = 'ggplot' # A clean style for visualizations
sns.set_style("whitegrid")


def load_and_clean_data(file_path):
    """
    Loads the CSV file and performs initial data cleaning and preparation.
    """
    print(f"--- Loading data from {file_path} ---")
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the file path.")
        return None

    print(f"Initial shape: {df.shape}")
    print("\n--- Initial Data Types ---")
    print(df.dtypes)

    # 1. Convert 'album_release_date' to datetime objects
    # Handle mixed date formats (e.g., 'YYYY-MM-DD' vs 'YYYY') by coercing errors
    df['album_release_date'] = pd.to_datetime(df['album_release_date'], errors='coerce')
    
    # Extract the year for trend analysis
    df['release_year'] = df['album_release_date'].dt.year

    # 2. Handle missing values (e.g., Artist Genres)
    # Replace 'N/A' genres with a standard string like 'Unknown'
    df['artist_genres'] = df['artist_genres'].replace('N/A', 'Unknown').fillna('Unknown')
    
    # Drop rows where essential numerical data is missing
    df.dropna(subset=['track_popularity', 'track_duration_min', 'release_year'], inplace=True)

    # 3. Data type check after cleaning
    df['release_year'] = df['release_year'].astype(int)

    print(f"\nShape after cleaning and dropping NAs: {df.shape}")
    print("--- Data Cleaning Complete ---")
    return df

def perform_eda(df):
    """
    Performs Exploratory Data Analysis (EDA) and prints key statistics.
    """
    print("\n" + "="*50)
    print("--- Exploratory Data Analysis (EDA) ---")
    print("="*50)

    # 1. Summary Statistics for numerical columns
    print("\n--- Summary Statistics (Track Popularity, Duration) ---")
    print(df[['track_popularity', 'track_duration_min', 'artist_popularity']].describe().T)

    # 2. Most Popular Artists
    print("\n--- Top 10 Most Popular Artists (by average track popularity) ---")
    top_artists = df.groupby('artist_name')['track_popularity'].mean().sort_values(ascending=False).head(10)
    print(top_artists.round(1))

    # 3. Most Popular Tracks
    print("\n--- Top 5 Most Popular Tracks ---")
    top_tracks = df.sort_values(by='track_popularity', ascending=False).head(5)
    print(top_tracks[['track_name', 'artist_name', 'track_popularity']])

    # 4. Album Type Distribution
    print("\n--- Album Type Distribution ---")
    print(df['album_type'].value_counts())

    # 5. Longest Tracks
    print("\n--- Top 5 Longest Tracks (in minutes) ---")
    longest_tracks = df.sort_values(by='track_duration_min', ascending=False).head(5)
    print(longest_tracks[['track_name', 'artist_name', 'track_duration_min']])


def generate_visualizations(df):
    """
    Generates and saves relevant visualizations to illustrate the data.
    """
    plt.style.use(PLOT_STYLE)
    print("\n" + "="*50)
    print("--- Generating Visualizations ---")
    print("="*50)

    # 1. Distribution of Track Popularity
    plt.figure(figsize=(10, 6))
    sns.histplot(df['track_popularity'], kde=True, bins=30, color='teal')
    plt.title('Distribution of Track Popularity Scores')
    plt.xlabel('Track Popularity (0-100)')
    plt.ylabel('Number of Tracks')
    plt.tight_layout()
    plt.savefig('1_track_popularity_distribution.png')
    plt.close()
    print("Saved '1_track_popularity_distribution.png'")
    # 

    # 2. Track Duration vs. Popularity (Scatter Plot)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='track_duration_min', y='track_popularity', data=df, alpha=0.5, color='coral')
    plt.title('Track Duration vs. Popularity')
    plt.xlabel('Track Duration (Minutes)')
    plt.ylabel('Track Popularity')
    plt.xlim(0, df['track_duration_min'].quantile(0.99)) # Limit x-axis to 99th percentile for clarity
    plt.tight_layout()
    plt.savefig('2_duration_vs_popularity_scatter.png')
    plt.close()
    print("Saved '2_duration_vs_popularity_scatter.png'")
    # 

    # 3. Popularity Trend over Time (by release year)
    # Calculate median popularity per year (using median to reduce outlier impact)
    popularity_over_time = df.groupby('release_year')['track_popularity'].median().reset_index()
    
    # Filter for years with a reasonable number of releases to avoid noise
    release_counts = df['release_year'].value_counts()
    valid_years = release_counts[release_counts > 50].index
    popularity_over_time = popularity_over_time[popularity_over_time['release_year'].isin(valid_years)]
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='release_year', y='track_popularity', data=popularity_over_time, marker='o', color='indigo')
    plt.title('Median Track Popularity Trend by Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Median Track Popularity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('3_popularity_trend_by_year.png')
    plt.close()
    print("Saved '3_popularity_trend_by_year.png'")
    # 


    # 4. Artist Popularity by Album Type
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='album_type', y='artist_popularity', data=df)
    plt.title('Artist Popularity by Album Type')
    plt.xlabel('Album Type')
    plt.ylabel('Artist Popularity')
    plt.tight_layout()
    plt.savefig('4_artist_popularity_by_album_type.png')
    plt.close()
    print("Saved '4_artist_popularity_by_album_type.png'")
    # 

    print("\n--- All visualizations saved successfully (PNG files) ---")


def main():
    """
    Main function to run the entire analysis pipeline.
    """
    # 1. Load, Clean, and Prepare Data
    spotify_df = load_and_clean_data(FILE_PATH)

    if spotify_df is not None:
        # 2. Perform Exploratory Data Analysis
        perform_eda(spotify_df)

        # 3. Generate Visualizations
        generate_visualizations(spotify_df)
    
    print("\n" + "="*50)
    print("--- Analysis Complete ---")
    print("The results are printed to the console, and charts are saved as PNG files.")
    print("="*50)


if __name__ == "__main__":

    main()


