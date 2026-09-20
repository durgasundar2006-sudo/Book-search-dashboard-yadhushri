# 📚 Book Search Dashboard

A Streamlit-based Book Search Dashboard that uses the Open Library Search API to search and display book information.

## 📌 Project Overview

This project allows users to search for books using a title, author name, or keyword. The application fetches real-time book information from the Open Library API and displays the results in a simple dashboard.

## ✨ Features

- Search books by title, author, or keyword
- Display book covers
- Display book title
- Display author information
- Display publication year
- Display publisher
- Display edition count
- Open the book on Open Library
- Quick search suggestions
- Handle empty searches
- Handle API and network errors

## 🛠️ Technologies Used

- Python
- Streamlit
- Open Library Search API
- JSON
- unittest

## 🔗 API Used

Open Library Search API:

https://openlibrary.org/search.json

## 📂 Project Structure

```text
Book-search-dashboard-yadhushri/
│
├── app.py
├── test app.py
├── requirements.txt
├── .gitignore
└── README.md
## ▶️ How to Run

1. Install Python on your system.
2. Install the required packages:

pip install -r requirements.txt

3. Run the Streamlit application:

streamlit run app.py

4. The application will open in your web browser.
## 🧪 Testing

The project includes automated tests for:

- Valid book searches
- Empty searches
- No-result searches
- Network errors
- Timeout handling
- Missing API fields
- Book data formatting
## ⚠️ Current Limitations

- No database or persistent storage
- No user authentication
- No favourites or search history
- No advanced filtering
- No pagination
## 🚀 Future Improvements

- Add search filters
- Add sorting options
- Add pagination
- Add favourites
- Add search history
- Add SQLite database
- Improve responsive UI
## 👩‍💻 Author

Yadhushri B. S
