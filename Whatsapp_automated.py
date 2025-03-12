from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
import time

# Path to Chrome profile for selenium to use
CHROME_PROFILE_PATH = r"C:\Users\rokas\AppData\Local\Google\Chrome\User Data\Default" # Replace with your path

def send_whatsapp_message(phone_number, message):
    # Open Chrome and navigate to WhatsApp Web

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Make the WhatsApp URL with the phone number and message
        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
        
        driver.get(whatsapp_url)
        
        # Wait for the "Continue to Chat" button to appear if the contact is new and click it
        wait = WebDriverWait(driver, 10)
        time.sleep(3)  # Pause to let the page do load

        try:
            continue_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//a[contains(@href, 'web.whatsapp.com/send?phone=')]"
                ))
            )
            continue_button.click()
            time.sleep(5)  # let the chat load
        except:
            # If "Continue to Chat" button does not appear, it's likely an existing contact
            pass
        
        # Find the text box and send the message
        
        send_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_button.click() # Click the send button
        
        print(f"Message sent to {phone_number}!")
        time.sleep(3)
        
    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")
    finally:
        driver.quit() # Close the browser window

# Test the function
if __name__ == "__main__":
    test_number = "44XXXXXXXXXX"  # Replace with a valid phone number
    test_message = "Hello!" # Replace with your message
    send_whatsapp_message(test_number, test_message) 
