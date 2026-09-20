# 📚 Book Search Dashboard

A Streamlit-based Book Search Dashboard that allows users to search for books using the Open Library Search API.

## 📌 About the Project

The Book Search Dashboard is a web-based application developed using Python and Streamlit.

It allows users to search for books using a book title, author name, or keyword. The application retrieves real-time book information from the Open Library Search API and displays the results in a simple dashboard.

---

## 🎯 Objectives

- To create a simple book search application.
- To learn how to work with a real-time API.
- To understand JSON data handling in Python.
- To display API data using Streamlit.
- To provide useful book information through a simple interface.

---

## ✨ Features

- Search books by title
- Search books by author
- Search books using keywords
- Display book covers
- Display book title
- Display author name
- Display publication year
- Display publisher
- Display edition count
- Open the book on Open Library
- Quick search options
- Error handling for API and network problems

---

## 🛠️ Technologies Used

| Technology | Usage |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Open Library Search API | Fetching book information |
| JSON | Handling API response data |
| unittest | Testing the application |
| GitHub | Source code management |

---

## 🔗 API Used

### Open Library Search API

This project uses the Open Library Search API to retrieve book information.

API:

https://openlibrary.org/search.json

The application sends the user's search query to the API and processes the JSON response to display book details.

---

## 🔄 How the Project Works

```text
User enters search
        ↓
Streamlit interface
        ↓
Search query
        ↓
Open Library Search API
        ↓
JSON response
        ↓
Python processes the data
        ↓
Book information displayed

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

👩‍💻 Author
Yadhushri B. S
Course: B.Tech Computer Science and Engineering
Year: 3rd Year
College:  WOMEN'S ENGINEERING COLLEGE, PONDICHERRY 
📚 Project Information
Project: Book Search Dashboard
Domain: Web Application
Technology: Python, Streamlit
API: Open Library Search API
Project Type: Academic / Student Project
