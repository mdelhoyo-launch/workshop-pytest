import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search(driver):
    # Step 1: Open the Google homepage
    driver.get("https://www.google.com")

    # Step 2: Type the search query into the search bar
    search_box = driver.find_element(By.NAME, "q")
    search_query = "Python"
    search_box.send_keys(search_query)

    # Step 3: Submit the search
    search_box.send_keys(Keys.RETURN)

    # Step 4: Assert that the search results page shows results for the query
    try:
        # Wait for the results page to load and display the results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # Get the title of the results page
        assert search_query in driver.title

        # Alternatively, verify that the search query is present in the results
        results = driver.find_elements(By.XPATH, f"//span[contains(text(), '{search_query}')]")
        assert len(results) > 0, "No results found for the query"

    except Exception as e:
        # If the assertion fails, print an error message
        print(f"Test failed: {e}")
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
