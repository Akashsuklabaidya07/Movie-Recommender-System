# Movie Recommender System

A content-based movie recommender system built using Machine Learing Streamlit  and The Movie Database (TMDb) API. The system recommends similar movies based on the input movie selected by the user and displays posters fetched from TMDb API.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [API Key Setup](#api-key-setup)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgement](#Acknowledgement)

## Overview
The Movie Recommender System is designed to help users find similar movies based on their preferences. Users can select a movie from the dropdown list, and the system will provide a list of recommended movies along with their posters, fetched dynamically from the TMDb API.

## Features
- **Movie Selection**: Users can choose a movie from a list of available titles.
- **Recommendations**: The system suggests 5 similar movies based on content similarity.
- **Posters**: Displays movie posters for each recommended title, fetched from the TMDb API.
- **Responsive Layout**: The recommendations are displayed neatly using Streamlit columns for better readability.

## Installation

### Prerequisites
- Python 3.x
- Streamlit
- Pandas
- Requests
- Pickle

### Clone the repository
```bash
git clone https://github.com/Akashsuklabaidya07/movie-recommender-system.git
cd movie-recommender-system
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### streamlit run app.py
```bash
streamlit run app.py
```

## Usage
Clone this repository and install the required dependencies.
Run the Streamlit app locally.
Select a movie from the dropdown list.
Click the Recommended Movies button to view movie recommendations with posters.

## Technologies Used
Python: Core logic for building the recommendation system.
Streamlit: Web framework for building the interactive user interface.
TMDb API: For fetching movie posters and additional movie details.
Pandas: Data processing and handling.
Pickle: For loading precomputed similarity models.

## Project Structure
```bash
.
├── app.py                      # Main application file with Streamlit code
├── movie_dict.pkl              # Pickled dictionary containing movie data
├── similarity.pkl              # Precomputed movie similarity matrix
├── README.md                   # Project README file
├── requirements.txt            # Python dependencies
└── .gitignore                  # Files to ignore in Git

```
## API Key Setup
To fetch movie posters, I will need to get an API key from The Movie Database (TMDb).

Sign up on the TMDb website and request an API key.
Replace the 89d3253dc7dc25b951c36c8f3644e9c5 in the code with your actual API key.
```bash
response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=89d3253dc7dc25b951c36c8f3644e9c5&language=en-US')
```
## Future Enhancements
Add the ability to filter recommendations based on genre or year.
Implement collaborative filtering for more personalized recommendations.
Include movie details like ratings and synopsis in the output.
Improve the UI by adding animations or a better design layout..

## Contributing
Contributions are welcome! Feel free to open a pull request or issue to suggest improvements.

## License
This project is licensed under the MIT License 

## Acknowledgments
The Movie Database (TMDB) for the movie data and posters.
The Python and Streamlit communities for their excellent documentation and tools.





