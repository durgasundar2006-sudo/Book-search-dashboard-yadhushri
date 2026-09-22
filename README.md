# 📚 Book Search Dashboard

The Book Search Dashboard is a Streamlit-based web application that allows users to search and explore book information using the Open Library Search API.

The application provides a simple and user-friendly interface where users can search for books using a title, author name, or keyword. The retrieved book information is displayed in an organized format along with available book cover images and relevant details.

The project demonstrates the practical use of Python, Streamlit, API integration, and JSON data processing to develop a real-time book search application.

---

## 🎯 Objective of the Application

The main objective of this application is to provide a simple and convenient platform for searching and exploring book information.

The application is designed to:

- Search for books using a title, author name, or keyword.
- Retrieve book information from the Open Library Search API.
- Process the JSON response received from the API.
- Display relevant book information in an organized format.
- Display available book cover images.
- Provide available Open Library links for books.
- Allow users to explore multiple search results based on their query.

---

## 🛠️ Tools and Technologies Used

### Application Development

| Technology | Purpose |
|---|---|
| Python | Used as the core programming language for developing the application. |
| Streamlit | Used to create the interactive Book Search Dashboard. |
| Open Library Search API | Used to retrieve book information based on user search queries. |
| JSON | Used to process and handle the data received from the API. |
| urllib | Used to send API requests and retrieve data from the Open Library API. |

### Development Tool

| Tool | Purpose |
|---|---|
| Google AI Studio | Used as a development assistance tool for generating, improving, and working with the application code. |

### Version Control and Repository

| Technology | Purpose |
|---|---|
| Git | Used for version control and tracking changes in the project. |
| GitHub | Used for storing, managing, and sharing the project source code. |

---

## 🙏 Acknowledgements

### Academic

This project was developed with the support, guidance, and encouragement received during the learning and development process. I would like to express my sincere gratitude to:

**Women's Engineering College, Lawspet** — For providing a supportive academic environment and the resources required for learning and project development.

**Department of Computer Science and Engineering** — For providing fundamental technical knowledge and learning opportunities that supported the development of this project.

**SARAVANAN** — For providing valuable mentorship, continuous encouragement, constructive feedback, and technical guidance throughout the development of this project.

### Open Source

This project benefits from publicly available APIs, open-source technologies, documentation, and developer resources.

**Open Library** — For providing the Search API used to retrieve book information for the application.

**Python and Streamlit Communities** — For providing documentation, libraries, tutorials, and development resources that supported the implementation of this project.

### Additional Thanks

I would also like to thank the open-source developer community for creating and maintaining useful tools and resources that support learning and application development.

---

## 👩‍💻 Author

**Name:** Yadhushri B.S

**Course:** B.Tech – Computer Science and Engineering

**Year:** III Year

**College:** Women's Engineering College

**Project Type:** Individual Project

**Project Title:**  
Book Search Dashboard

**Technology:** Python + Streamlit

**API:** Open Library Search API

---

## 🎨 Color Reference

The Book Search Dashboard uses a clean and minimal color palette with a very light blue background, white content sections, and red interactive buttons to provide a simple and comfortable user experience.

| Color Role | Hex Code |
|---|---|
| Light Blue Background | `#EAF6FF` |
| White Content / Cards | `#FFFFFF` |
| Red Buttons | `#E53935` |
| Dark Gray Text | `#333333` |
| Light Gray Sections | `#F5F5F5` |

---

## 🌐 Live Demo

The Book Search Dashboard is available as an online web application. Users can access the application through a web browser and search for book information using the Open Library Search API.

**Live Demo:**

https://student-library-847263.ai.studio

---

# 🚀 Project Preview

The following screenshots demonstrate the main screens and functionalities of the Book Search Dashboard.

## 🔍 Book Search Dashboard

The main dashboard provides a simple and user-friendly interface where users can enter a book title, author name, or keyword to search for relevant books.

**Screenshot:**

![Book Search Dashboard](images/book.png)

---

## 📚 Book Search Results

The search results section displays books matching the user's search query along with the available information retrieved from the Open Library Search API.

**Screenshot:**

![Book Search Result](images/book2.png)

---

## 📖 Book Information

The application displays available information about each book, including the book title, author, publication year, publisher, and other relevant details provided by the API.

**Screenshot:**

![Book Information](images/book4.png)

---

## 🖼️ Book Cover Display

Available book cover images are displayed along with the corresponding search results, making it easier for users to identify the books.

**Screenshot:**

![Book Cover Display](images/book5.png)

---

# 🏗️ System Architecture

The Book Search Dashboard follows a simple architecture in which the user interacts with the Streamlit interface. The application sends the search request to the Open Library Search API, receives the response in JSON format, processes the required information, and displays the book results to the user.

**System Architecture Diagram:**

## 🏗️ System Architecture

The system architecture of the Book Search Dashboard is shown below.

![System Architecture](images/system-architecture.png)

---

# 🔄 System Flowchart

The system follows a simple sequence from entering a search query to displaying the retrieved book information.

## 🔄 System Flowchart

The system flow of the Book Search Dashboard is shown below.

![System Flowchart](images/system-flowchart.png)

---
🔁 Data Flow Diagram
The Data Flow Diagram represents how the search query and book information move between the user, application, and Open Library Search API.

## 🔁 Data Flow Diagram

The data flow of the Book Search Dashboard is shown below.

![Data Flow Diagram](images/data-flow-diagram.png)

---

##🗂️ Project Structure
The project contains the main Streamlit application file along with the required documentation and configuration files.
Book-search-dashboard-yadhushri/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
##⚙️ Installation Steps
Step 1: Clone Repository
Clone the project repository from GitHub using:
git clone https://github.com/durgasundar2006-sudo/Book-search-dashboard-yadhushri.git
Step 2: Navigate to Project Folder
cd Book-search-dashboard-yadhushri
Step 3: Install Required Dependencies
Install the required Python packages using:
pip install -r requirements.txt

---

##▶️ How to Run the Application:
Run the Streamlit application using:
streamlit run app.py
After running the command, Streamlit will provide a local URL.
Open the displayed URL in a web browser to access the Book Search Dashboard.

---
##🚀 Key Project Features
✅ Search books using title, author, or keyword
✅ Retrieve book information using the Open Library Search API
✅ Process JSON data received from the API
✅ Display multiple book search results
✅ Display book title and author information
✅ Display publication year and publisher information when available
✅ Display available book cover images
✅ Provide available Open Library links
✅ Simple and user-friendly Streamlit dashboard
✅ Real-time API-based book search

---

##🔌 Open Library API Integration
The project uses the Open Library Search API to retrieve book information based on the search query entered by the user.
The application sends the search request to the Open Library API and receives the matching book records in JSON format. The required information is then extracted from the response and displayed through the Streamlit dashboard.
The API allows the application to retrieve book information without maintaining a separate database of book records.

---

##🔄 Application Workflow
The application processes a book search through the following pipeline:
Enter Book Title / Author / Keyword
              ↓
       Streamlit Dashboard
              ↓
        Create API Request
              ↓
     Open Library Search API
              ↓
        Receive JSON Data
              ↓
       Process Book Details
              ↓
      Display Search Results
              ↓
        View Book Information

 ---
 
##📊 Search Options
The application allows users to search for books using different types of search information.
Book Title
Users can enter the title of a book to retrieve matching book records from the Open Library Search API.
Author
Users can enter an author's name to find books associated with that author.
Keyword
Users can enter a keyword to discover books related to the provided search term.

---

##📖 Book Details Displayed
The application displays the available information retrieved from the Open Library Search API.
The displayed information may include:
Book Title
Author Name
Publication Year
Publisher
Book Cover
Open Library Link
The availability of individual details depends on the information provided by the Open Library API.

---

##🧩 Application Components
The Book Search Dashboard consists of several components that work together to provide the book search functionality.
Search Interface
The search interface allows users to enter a title, author name, or keyword and initiate a book search.
API Request Handler
The API request component sends the user's search query to the Open Library Search API and retrieves the corresponding response.
JSON Data Processing
The application processes the JSON response and extracts the relevant book information required for display.
Results Display
The processed information is presented through the Streamlit interface in an organized and readable format.
Book Cover Display
When a cover image is available, the application displays it along with the corresponding book information.

---

##🌐 Deployment

The Book Search Dashboard is made available as an online web application. The project source code is maintained in GitHub, while Streamlit is used to run and present the interactive dashboard.
Technology
Purpose
Streamlit
Used to run and present the interactive web application.
GitHub
Used to maintain and manage the project source code.

----

##📌 GitHub Repository

The complete source code and project documentation are maintained in the GitHub repository.
Repository:
https://github.com/durgasundar2006-sudo/Book-search-dashboard-yadhushri⁠�

---

##❓ FAQ

1. What is the Book Search Dashboard?
The Book Search Dashboard is a Streamlit-based web application that allows users to search and explore book information using the Open Library Search API.
2. What can users search for?
Users can search for books using a book title, author name, or keyword.
3. Where does the book information come from?
The application retrieves book information from the Open Library Search API.
4. Does the application use a database?
No. The application retrieves book information directly from the Open Library Search API and does not require a separate database.
5. What information is displayed for each book?
Depending on the information available from the API, the application can display the book title, author, publication year, publisher, cover image, and Open Library link.
6. Does the application require authentication?
No. The application does not require user authentication or account creation to perform book searches.
7. What technologies are used in this project?
The project uses Python, Streamlit, the Open Library Search API, JSON data processing, Git, and GitHub.
8. What development tool was used for this project?
Google AI Studio was used as a development assistance tool for generating, improving, and working with the application code.
9. Where is the source code maintained?
The source code and project documentation are maintained in the GitHub repository.
10. Can the project be improved in the future?
Yes. Future improvements may include advanced filtering, category-based searching, sorting options, detailed book pages, favorites or bookmarks, and additional book information.

---

##⭐ Conclusion

The Book Search Dashboard demonstrates the practical use of Python, Streamlit, and API integration to create a real-time book search application.
By connecting the Open Library Search API with an interactive Streamlit interface, the project provides users with an organized way to search for books and explore the available book information.
The project also demonstrates the practical use of JSON data processing, API communication, web application development, and GitHub-based project management.

