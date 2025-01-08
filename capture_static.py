from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# URL of the running Streamlit app
STREAMLIT_URL = "http://localhost:8501"

# Path to save the static HTML
OUTPUT_PATH = "static_site/index.html"

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

# Open the Streamlit app
driver.get(STREAMLIT_URL)
time.sleep(5)  # Wait for the app to fully load

# Save the rendered HTML
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()
print(f"Static HTML saved to {OUTPUT_PATH}")