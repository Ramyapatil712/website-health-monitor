import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def main():
    url1 = "https://topfactor.org/"
    expected_text_url1 = 'TOP Factor'

    url2 = "https://lifecyclejournal.org/"
    expected_text_url2 = 'Adding trustworthiness, from conception through completion'

    url3 = "https://metascience.info/"
    expected_text_url3 = 'Metascience 2025 Conference'

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url1)
        print(f"Loaded: {url1}")
        page_source = driver.page_source

        if expected_text_url1 not in page_source:
            raise Exception(f"Expected text '{expected_text_url1}' not found on page")

        print("✅ Website is up and responding as expected.")
    except Exception as e:
        print(f"❌ Monitoring failed: {e}")
        sys.exit(1)
    try:
        driver.get(url2)
        print(f"Loaded: {url2}")
        page_source = driver.page_source

        if expected_text_url2 not in page_source:
            raise Exception(f"Expected text '{expected_text_url2}' not found on page")

        print("✅ Website is up and responding as expected.")
    except Exception as e:
        print(f"❌ Monitoring failed: {e}")
        sys.exit(1)

    try:
        driver.get(url3)
        print(f"Loaded: {url3}")
        page_source = driver.page_source

        if expected_text_url3 not in page_source:
            raise Exception(f"Expected text '{expected_text_url3}' not found on page")

        print("✅ Website is up and responding as expected.")
    except Exception as e:
        print(f"❌ Monitoring failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()