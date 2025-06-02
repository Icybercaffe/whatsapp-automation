from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from fetch_message import get_love_message
import os
from dotenv import load_dotenv

load_dotenv()

def send_message_now():
    print("Starting script...")
    message = get_love_message()
    message = ''.join(c for c in message if ord(c) <= 0xFFFF)
    print(f"Message fetched (filtered): {message}")
    phone_number = os.getenv("PHONE_NUMBER")  

    print("Setting up Chrome...")
    session_path = os.getenv("SESSION_PATH")
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={session_path}")
    driver = webdriver.Chrome(options=chrome_options)
    print("Chrome opened successfully.")

    print(f"Navigating to WhatsApp: {phone_number}")
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")

    print("Waiting for chat to load...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="main"]'))
    )
    print("Chat pane loaded.")

    print("Waiting for chat input box...")
    try:
        input_box = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true" and @aria-label="Type a message"]'))
        )
        print(f"Input box attributes: {input_box.get_attribute('outerHTML')}")
        driver.execute_script("arguments[0].focus(); arguments[0].innerText = '';", input_box)
        input_box.send_keys(message)
        print("Message typed in chat.")
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]/parent::button'))
        )
        driver.execute_script("arguments[0].click();", send_button)
        print("Send button clicked.")
    except Exception as e:
        print(f"Error during interaction: {e}")
        driver.save_screenshot("error_screenshot.png")
        textboxes = driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')
        for i, tb in enumerate(textboxes):
            print(f"Textbox {i}: {tb.get_attribute('outerHTML')}")
        driver.quit()
        return

    time.sleep(5)
    print("Closing Chrome...")
    driver.quit()

if __name__ == "__main__":
    send_message_now()
