"""
Automated Test Suite for Book Search Dashboard
Traceable to REQ-01 through REQ-05 and TEST-01 through TEST-08.
Uses pure Python standard library for zero-dependency test execution.
"""

import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import json
from app import fetch_books_from_api, format_book_item

class TestBookSearchDashboard(unittest.TestCase):

    # TEST-01: Valid book title search
    @patch('urllib.request.urlopen')
    def test_01_valid_book_title_search(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_payload = {
            "numFound": 1,
            "docs": [
                {
                    "title": "Clean Code",
                    "author_name": ["Robert C. Martin"],
                    "first_publish_year": 2008,
                    "cover_i": 12345
                }
            ]
        }
        mock_response.read.return_value = json.dumps(mock_payload).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        
        result = fetch_books_from_api("Clean Code", limit=10)
        self.assertTrue(result["success"])
        self.assertEqual(result["status_code"], 200)
        self.assertEqual(result["data"]["numFound"], 1)
        self.assertEqual(result["data"]["docs"][0]["title"], "Clean Code")
        mock_urlopen.assert_called_once()

    # TEST-02: Author-name or keyword search
    @patch('urllib.request.urlopen')
    def test_02_author_or_keyword_search(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_payload = {
            "numFound": 2,
            "docs": [
                {"title": "1984", "author_name": ["George Orwell"]},
                {"title": "Animal Farm", "author_name": ["George Orwell"]}
            ]
        }
        mock_response.read.return_value = json.dumps(mock_payload).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = fetch_books_from_api("George Orwell", limit=10)
        self.assertTrue(result["success"])
        self.assertEqual(len(result["data"]["docs"]), 2)

    # TEST-03: Empty search input validation (REQ-04)
    def test_03_empty_search_query_handling(self):
        result_empty = fetch_books_from_api("")
        self.assertFalse(result_empty["success"])
        self.assertIn("Empty search query", result_empty["error"])

        result_spaces = fetch_books_from_api("   ")
        self.assertFalse(result_spaces["success"])
        self.assertIn("Empty search query", result_spaces["error"])

    # TEST-04: Search with no matching results (REQ-04)
    @patch('urllib.request.urlopen')
    def test_04_no_matching_results(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_payload = {
            "numFound": 0,
            "docs": []
        }
        mock_response.read.return_value = json.dumps(mock_payload).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = fetch_books_from_api("xyznonexistentbook12345999", limit=10)
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["numFound"], 0)
        self.assertEqual(len(result["data"]["docs"]), 0)

    # TEST-05: Open Library API/network failure (REQ-05)
    @patch('urllib.request.urlopen')
    def test_05_network_failure_timeout(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("timed out")
        result = fetch_books_from_api("Python", limit=10)
        self.assertFalse(result["success"])
        self.assertIn("timed out", result["error"].lower())

    @patch('urllib.request.urlopen')
    def test_05b_network_connection_error(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
        result = fetch_books_from_api("Python", limit=10)
        self.assertFalse(result["success"])
        self.assertIn("connection", result["error"].lower())

    # TEST-06: API response missing some optional book information (REQ-03)
    def test_06_missing_optional_fields(self):
        sparse_doc = {
            "title": "Minimal Book"
        }
        formatted = format_book_item(sparse_doc)
        self.assertEqual(formatted["title"], "Minimal Book")
        self.assertEqual(formatted["author"], "Unknown Author")
        self.assertEqual(formatted["year"], "Not specified")
        self.assertIsNone(formatted["cover_url"])
        self.assertIsNone(formatted["publisher"])

    # TEST-07: Successful display of returned book information (REQ-03)
    def test_07_full_field_extraction(self):
        full_doc = {
            "title": "The Pragmatic Programmer",
            "author_name": ["Andrew Hunt", "David Thomas"],
            "first_publish_year": 1999,
            "cover_i": 8234125,
            "publisher": ["Addison-Wesley"],
            "edition_count": 14,
            "key": "/works/OL257943W"
        }
        formatted = format_book_item(full_doc)
        self.assertEqual(formatted["title"], "The Pragmatic Programmer")
        self.assertEqual(formatted["author"], "Andrew Hunt, David Thomas")
        self.assertEqual(formatted["year"], "1999")
        self.assertEqual(formatted["cover_url"], "https://covers.openlibrary.org/b/id/8234125-M.jpg")
        self.assertEqual(formatted["publisher"], "Addison-Wesley")
        self.assertEqual(formatted["edition_count"], 14)
        self.assertEqual(formatted["link"], "https://openlibrary.org/works/OL257943W")

    # TEST-08: Basic end-to-end flow from student input to formatted card (REQ-01 through REQ-05)
    @patch('urllib.request.urlopen')
    def test_08_end_to_end_flow(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_payload = {
            "numFound": 1,
            "docs": [
                {
                    "title": "Artificial Intelligence: A Modern Approach",
                    "author_name": ["Stuart Russell", "Peter Norvig"],
                    "first_publish_year": 1995,
                    "cover_i": 999123
                }
            ]
        }
        mock_response.read.return_value = json.dumps(mock_payload).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        
        # Step 1: Execute search API call
        res = fetch_books_from_api("Artificial Intelligence", limit=5)
        self.assertTrue(res["success"])
        
        # Step 2: Format items for presentation
        docs = res["data"]["docs"]
        self.assertEqual(len(docs), 1)
        card = format_book_item(docs[0])
        self.assertEqual(card["title"], "Artificial Intelligence: A Modern Approach")
        self.assertEqual(card["author"], "Stuart Russell, Peter Norvig")
        self.assertEqual(card["year"], "1995")
        self.assertIsNotNone(card["cover_url"])

if __name__ == "__main__":
    unittest.main()
