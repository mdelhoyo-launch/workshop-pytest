import pytest
from pages.youtube_home_page import YouTubeHomePage
from pages.youtube_search_results_page import YouTubeSearchResultsPage

def test_youtube_search(driver):
    home_page = YouTubeHomePage(driver)
    search_results_page = YouTubeSearchResultsPage(driver)
    search_query = "Selenium Python Tutorial"

    # Step 1: Open the YouTube homepage
    home_page.open()

    # Step 2: Type the search query into the search bar and submit
    home_page.search(search_query)

    # Step 3: Wait for the results page to load and display the results
    search_results_page.is_loaded()

    # Step 4: Assert that the search results page shows results for the query
    assert search_query in search_results_page.get_title()
    assert search_results_page.has_results(search_query)
