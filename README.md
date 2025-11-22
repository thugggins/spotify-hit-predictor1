Spotify Popularity Predictor 
------------------------------------------------------------------------

This is a single-file, interactive web application that demonstrates a simulated machine learning model's approach to predicting the popularity score of a Spotify track (on a scale of 0-100).
The application runs entirely in the browser using HTML, Tailwind CSS, and vanilla JavaScript, and relies on an embedded, static dataset for its predictions, meaning no live Spotify API key or token is required to run this demo.

Features
-------------------------------------------

Interactive Controls (New Flow): Use dynamic dropdowns to select an Artist, filter to a corresponding Genre, and finally choose a specific Track. The application then automatically loads and displays all corresponding track details, including Album Type, Artist Followers, Artist Popularity, Track Duration, and Explicit status.

Simulated ML Model: The prediction logic uses a simplified Linear Regression formula with pre-defined weights (coefficients) to demonstrate how different features contribute to the final score.

Two Operation Modes:
--------------------------------------------

- Track Selection Mode: Select a specific track from the embedded dataset. The track's features (such as Artist Popularity, Duration, Album Type) are loaded and locked for prediction.

- Custom Track Mode: Select the "Custom Track" option in the Track dropdown to run a prediction based on the features currently displayed (Artist Popularity, Track Duration, etc.), allowing you to evaluate a hypothetical combination of selected Artist and Genre features.

Real-Time Feedback: The predicted popularity score is displayed visually, along with a message summarizing the predicted success level (e.g., "Mega Hit Potential" or "Moderate Success").

Data & Transparency
-------------------------------------

Data Catalog: A transparent table at the bottom of the page displays the complete embedded dataset used for all predictions and lookups. Crucially, all missing data points (originally marked as NaN) are cleaned and displayed as "unknown" to ensure data completeness and readability.

Model Logic (Simulated)
----------------------------------------------------

The core prediction is calculated using a simplified formula based on four key features:

$$\text{Popularity Score} = \text{Bias} + (\text{Artist Popularity} \times W_{AP}) + (\text{Duration} \times W_{D}) + (\text{Is Single} \times W_{S})$$

Where the predefined weights are:
---------------------------------------------
| Feature | Coefficient (Weight) | Explanation |
| :--- | :--- | :--- |
| Bias | +35.0 | Base popularity score. |
| Artist Popularity ($W_{AP}$) | +0.8 | Strongest positive driver. High artist popularity significantly increases track score. |
| Track Duration (Minutes) ($W_{D}$) | -1.5 | A slight penalty for non-standard duration, aiming to favor tracks around the average (3-4 minutes). |
| Is Single (Boolean) ($W_{S}$) | +5.0 | Bonus for tracks released as singles, reflecting increased promotion and focus. |

The final score is always capped between 0 and 100.

Setup and Running
-----------------------------------------
Since this is a single-file HTML application, no backend, server, or build step is required.

Download/Clone: Get the index.html file onto your local machine.

Open in Browser: Simply double-click the index.html file, or open it directly in any modern web browser.

Interact: Start selecting artists, genres, or custom tracks to see instant predictions.


