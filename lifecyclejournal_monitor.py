import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    url = "https://lifecyclejournal.org/"
    expected_text = 'Adding trustworthiness, from conception through completion'

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        print(f"Loaded: {url}")
        page_source = driver.page_source

        if expected_text not in page_source:
            raise Exception(f"Expected text '{expected_text}' not found on page")

        print("✅ Website is up and responding as expected.")
    except Exception as e:
        print(f"❌ Monitoring failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()