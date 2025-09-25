from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- CONFIG ---
URL = "https://lhr-agent.enteract.live/"
AGENT_EXTENSION = "10119"
PASSWORD = "1234"

# Start Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
time.sleep(2)

# --- STEP 1: Enter Agent Extension ---
agent_input = driver.find_element(By.ID, "name")   # Or By.NAME, "extension"
agent_input.send_keys(AGENT_EXTENSION)

login_button1 = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
login_button1.click()
time.sleep(2)

# --- STEP 2: Enter Password ---
# Adjust locator if ID/Name is different (need password field HTML snippet to confirm)
password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys(PASSWORD)

login_button2 = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
login_button2.click()
time.sleep(5)

print("✅ Logged in successfully. You are now on:", driver.title)

# --- Stay logged in ---
# Script won’t quit, keeps browser open for you to continue.
while True:
    time.sleep(5)   # Keeps the session alive

