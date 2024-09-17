# Movie Recommender System

A content-based movie recommender system built using Python, Streamlit, and The Movie Database (TMDb) API. The system recommends similar movies based on the input movie selected by the user and displays posters fetched from TMDb API.

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

## Overview
The Movie Recommender System is designed to help users find similar movies based on their preferences. Users can select a movie from the dropdown list, and the system will provide a list of recommended movies along with their posters, fetched dynamically from the TMDb API.

## Features
- **Movie Selection**: Users can choose a movie from a list of available titles.
- **Recommendations**: The system suggests 5 similar movies based on content similarity.
- **Posters**: Displays movie posters for each recommended title, fetched from the TMDb API.
- **Responsive Layout**: The recommendations are displayed neatly using Streamlit columns for better readability.

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Streamlit
- Pandas
- Requests
- Pickle

### Clone the repository
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system

