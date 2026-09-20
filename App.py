"""
Book Search Dashboard
====================
A student-friendly web dashboard to search for books and view basic publication details
in real-time using the public Open Library Search API.

Technology: Python 3 + Streamlit
Data Source: Open Library Search API (https://openlibrary.org/search.json)
Persistence: None (transient search state)
Authentication: None (student accessible without login)
"""

try:
    import streamlit as st
except ImportError:
    st = None

import json
import urllib.request
import urllib.parse
import urllib.error
from typing import Dict, Any, List, Optional

# Constants
OPEN_LIBRARY_API_URL = "https://openlibrary.org/search.json"
DEFAULT_TIMEOUT_SECONDS = 10
COVER_IMAGE_BASE_URL = "https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"

def fetch_books_from_api(query: str, limit: int = 15) -> Dict[str, Any]:
    """
    Sends a GET request to the Open Library Search API for the given search query.
    Uses standard library urllib (compatible with all standard Python 3 installations)
    with clean error handling for timeouts, HTTP errors, and connection issues.
    
    Args:
        query: Book title, author name, or keyword entered by the student.
        limit: Maximum number of results to retrieve.
        
    Returns:
        A dictionary containing:
            - 'success' (bool): True if HTTP request succeeded, False otherwise.
            - 'status_code' (int): HTTP status code.
            - 'data' (dict or None): Parsed JSON data if successful.
            - 'error' (str or None): Error message if request failed.
    """
    clean_query = query.strip()
    if not clean_query:
        return {
            "success": False,
            "status_code": 400,
            "data": None,
            "error": "Empty search query. Please enter a book title, author, or keyword."
        }

    encoded_params = urllib.parse.urlencode({"q": clean_query, "limit": limit})
    full_url = f"{OPEN_LIBRARY_API_URL}?{encoded_params}"
    
    headers = {
        "User-Agent": "BookSearchDashboard/1.0 (Student Project; educational use)"
    }
    
    req = urllib.request.Request(full_url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT_SECONDS) as response:
            status_code = response.getcode()
            if status_code == 200:
                raw_data = response.read().decode("utf-8")
                try:
                    json_data = json.loads(raw_data)
                    return {
                        "success": True,
                        "status_code": 200,
                        "data": json_data,
                        "error": None
                    }
                except ValueError:
                    return {
                        "success": False,
                        "status_code": 200,
                        "data": None,
                        "error": "The Open Library API returned an unreadable or non-JSON response."
                    }
            else:
                return {
                    "success": False,
                    "status_code": status_code,
                    "data": None,
                    "error": f"Open Library API returned an HTTP error (Status {status_code})."
                }
                
    except urllib.error.HTTPError as e:
        return {
            "success": False,
            "status_code": e.code,
            "data": None,
            "error": f"Open Library API returned HTTP error: {e.code} {e.reason}"
        }
    except urllib.error.URLError as e:
        reason_str = str(e.reason).lower()
        if "timed out" in reason_str:
            return {
                "success": False,
                "status_code": None,
                "data": None,
                "error": "The request timed out while connecting to the Open Library API. Please check your internet connection."
            }
        return {
            "success": False,
            "status_code": None,
            "data": None,
            "error": f"Failed to connect to the Open Library API: {e.reason}. Please verify your internet connection."
        }
    except Exception as e:
        return {
            "success": False,
            "status_code": None,
            "data": None,
            "error": f"Network error occurred while fetching book data: {str(e)}"
        }

def format_book_item(doc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Safely extracts and formats book information from an Open Library document item.
    Handles missing or optional fields cleanly without raising KeyError or IndexError.
    """
    title = doc.get("title", "Untitled Book")
    
    # Authors
    authors = doc.get("author_name", [])
    author_display = ", ".join(authors) if isinstance(authors, list) and authors else "Unknown Author"
    
    # First publication year
    first_publish_year = doc.get("first_publish_year")
    year_display = str(first_publish_year) if first_publish_year else "Not specified"
    
    # Cover image ID
    cover_id = doc.get("cover_i")
    cover_url = COVER_IMAGE_BASE_URL.format(cover_id=cover_id) if cover_id else None
    
    # Publisher
    publishers = doc.get("publisher", [])
    publisher_display = publishers[0] if isinstance(publishers, list) and publishers else None
    
    # Edition count & Open Library Key
    edition_count = doc.get("edition_count", 0)
    ol_key = doc.get("key", "")
    ol_link = f"https://openlibrary.org{ol_key}" if ol_key else None
    
    return {
        "title": title,
        "author": author_display,
        "year": year_display,
        "cover_url": cover_url,
        "publisher": publisher_display,
        "edition_count": edition_count,
        "link": ol_link
    }

def main():
    """Main function rendering the Streamlit dashboard."""
    st.set_page_config(
        page_title="Book Search Dashboard",
        page_icon="📚",
        layout="wide"
    )
    
    # Header Section
    st.title("📚 Book Search Dashboard")
    st.markdown(
        "Welcome to the **Book Search Dashboard** for students. "
        "Enter a book title, author name, or subject keyword below to look up books "
        "in real-time from the **Open Library Search API**."
    )
    
    # Search Form (REQ-01)
    with st.form(key="search_form"):
        col1, col2 = st.columns([4, 1])
        with col1:
            search_query = st.text_input(
                label="Search Query",
                placeholder="e.g., Python Programming, To Kill a Mockingbird, George Orwell...",
                help="Type a title, author name, or subject keyword to search."
            )
        with col2:
            max_results = st.selectbox(
                label="Max Results",
                options=[10, 20, 30],
                index=0
            )
            
        submit_button = st.form_submit_button(label="🔍 Search Books", type="primary")
        
    # Quick suggestion buttons
    st.markdown("**Sample Student Queries:**")
    quick_cols = st.columns(4)
    sample_queries = [
        "Data Structures",
        "Clean Code",
        "Pride and Prejudice",
        "Artificial Intelligence"
    ]
    
    # Store query in session state if quick button clicked
    for idx, sample in enumerate(sample_queries):
        if quick_cols[idx].button(sample, key=f"quick_{idx}"):
            st.session_state["active_query"] = sample
            st.rerun()

    # Determine query to execute
    active_query = search_query.strip() if submit_button else st.session_state.get("active_query", "")
    
    # Clear session query once used
    if "active_query" in st.session_state and not submit_button:
        del st.session_state["active_query"]

    # Search Execution & Results Handling (REQ-02, REQ-03, REQ-04, REQ-05)
    if submit_button or active_query:
        # REQ-04: Empty Search Validation
        if not active_query:
            st.warning("⚠️ Please enter a book title, author name, or keyword before searching.")
            return

        # REQ-02: Show spinner while retrieving data from Open Library API
        with st.spinner(f"Contacting Open Library Search API for '{active_query}'..."):
            result = fetch_books_from_api(active_query, limit=max_results)
            
        # REQ-05: API / Network Failure Handling
        if not result["success"]:
            st.error(f"❌ **API Error:** {result['error']}")
            st.caption("Please verify your internet connectivity and ensure openlibrary.org is accessible.")
            return
            
        data = result["data"] or {}
        num_found = data.get("numFound", 0)
        docs: List[Dict[str, Any]] = data.get("docs", [])
        
        # REQ-04: No Results Handling
        if num_found == 0 or len(docs) == 0:
            st.info(f"ℹ️ No books found matching **'{active_query}'**. Please try a different title, author name, or spelling.")
            return
            
        # REQ-03 & REQ-04: Results Display
        st.success(f"✅ Found **{num_found:,}** matching books on Open Library (showing top {len(docs)}):")
        
        # Render Book Cards
        for idx, doc in enumerate(docs):
            book = format_book_item(doc)
            
            with st.container():
                st.markdown("---")
                c_img, c_info = st.columns([1, 4])
                
                with c_img:
                    if book["cover_url"]:
                        st.image(book["cover_url"], width=130)
                    else:
                        st.markdown(
                            "<div style='border: 1px dashed #bbb; border-radius: 6px; padding: 24px 8px; text-align: center; color: #888; background: #fafafa; font-size: 13px;'>"
                            "📖<br>Cover Not<br>Available"
                            "</div>",
                            unsafe_allow_html=True
                        )
                        
                with c_info:
                    st.subheader(book["title"])
                    st.markdown(f"👤 **Author(s):** {book['author']}")
                    st.markdown(f"📅 **First Published:** {book['year']}")
                    if book["publisher"]:
                        st.markdown(f"🏢 **Publisher:** {book['publisher']}")
                    if book["edition_count"] > 0:
                        st.markdown(f"📚 **Known Editions:** {book['edition_count']}")
                    if book["link"]:
                        st.markdown(f"[🔗 View on Open Library]({book['link']})")

    else:
        # Default Welcome State
        st.info("👆 Enter a book search query above or select one of the sample topics to start searching.")

if __name__ == "__main__":
    main()
