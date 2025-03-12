<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />

</head>

<body>
  <h1>WhatsApp Web Automation Using Selenium</h1>
  <p>This repository provides a Python script that automates sending WhatsApp messages via WhatsApp Web, using <strong>Selenium</strong> and <strong>webdriver-manager</strong>. It opens WhatsApp Web in a persistent Chrome session, allowing you to send predefined messages to any phone number in international format, without scanning a QR code each time.</p>

  <h2>Features</h2>
  <ul>
    <li>Uses an existing Chrome user profile to avoid repeated QR logins.</li>
    <li>Automatically handles the <em>“Continue to Chat”</em> button for new contacts.</li>
    <li>Sends messages to a specified phone number.</li>
    <li>Simple and straightforward Python code.</li>
  </ul>

  <h2>Prerequisites</h2>
  <ul>
    <li><strong>Python 3.7+</strong> installed</li>
    <li><strong>Google Chrome</strong> browser installed</li>
    <li>A <strong>Chrome user profile</strong> that’s already logged into WhatsApp Web</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone or download this repository.</li>
    <li>Open a terminal (or command prompt) in the project directory.</li>
    <li>Install dependencies:
      <pre><code>pip install selenium webdriver-manager</code></pre>
    </li>
    <li>
      Locate your Chrome user data folder. On Windows, it’s usually:
      <pre><code>C:\Users\[YourUser]\AppData\Local\Google\Chrome\User Data\Default</code></pre>
      Update the path in the script if needed.
    </li>
    <li>Make sure your Chrome version matches the ChromeDriver installed by <code>webdriver-manager</code> (this is usually handled automatically).</li>
  </ol>

  <h2>Usage</h2>
  <p>Open the <code>Whatsapp_automated.py</code> (or similar) file and adjust the following line to your own profile path:</p>
  <pre><code>CHROME_PROFILE_PATH = r"C:\Users\rokas\AppData\Local\Google\Chrome\User Data\Default"
</code></pre>

  <p>Then, specify a valid phone number in international format (without <code>+</code>), and your desired message:</p>
  <pre><code># Example usage at the bottom of the file:
if __name__ == "__main__":
    test_number = "44XXXXXXXXXX"  # Replace with a valid phone number
    test_message = "Hello!"       # Replace with your message
    send_whatsapp_message(test_number, test_message)
</code></pre>

  <p>Run the script:</p>
  <pre><code>python Whatsapp_automated.py
</code></pre>

  <h3>Notes</h3>
  <ul>
    <li>The first time you run this script with a new Chrome user profile, WhatsApp Web may require you to scan the QR code. Once scanned, you remain logged in.</li>
    <li>For new contacts, WhatsApp shows a <em>“Continue to Chat”</em> link. The script attempts to click it automatically.</li>
    <li>If you encounter <strong>NoSuchElementException</strong>, it may be because WhatsApp Web’s UI changed. Update the XPaths or CSS selectors accordingly.</li>
    <li>Be mindful of WhatsApp’s terms of service and spam policies. Use responsibly.</li>
  </ul>

  <h2>Source Code</h2>
  <pre><code>from selenium import webdriver
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
        whatsapp_url = f"https://web.whatsapp.com/send?phone={{phone_number}}&text={{encoded_message}}"
        
        driver.get(whatsapp_url)
        
        # Wait for the 'Continue to Chat' button to appear if the contact is new and click it
        wait = WebDriverWait(driver, 10)
        time.sleep(3)  # Pause to let the page load

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
            # If 'Continue to Chat' button does not appear, it's likely an existing contact
            pass
        
        # Find the Send button (data-icon='send') and click it
        send_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_button.click() # Click the send button
        
        print(f"Message sent to {{phone_number}}!")
        time.sleep(3)
        
    except Exception as e:
        print(f"Error sending message to {{phone_number}}: {{e}}")
    finally:
        driver.quit() # Close the browser window

# Test the function
if __name__ == "__main__":
    test_number = "44XXXXXXXXXX"  # Replace with a valid phone number
    test_message = "Hello!" # Replace with your message
    send_whatsapp_message(test_number, test_message)
</code></pre>

  <h2>License</h2>
  <p>This project is provided “as is” without warranty of any kind. Use at your own risk and ensure you adhere to WhatsApp’s policies.</p>

  <hr />
  <p><em>Happy Messaging!</em></p>
</body>
</html>
