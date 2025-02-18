from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by_type, identifier, timeout=10):
    """Wait for an element to be located."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by_type, identifier))
    )
