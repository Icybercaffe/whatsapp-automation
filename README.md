# WhatsApp Automation Bot

This is a Python automation project that sends WhatsApp messages using Selenium and OpenAI to fetch dynamic messages. The goal is to deliver simple, personalized automated messages such as greetings or reminders through WhatsApp Web when the computer starts.

## Features

- Opens WhatsApp Web in Google Chrome
- Fetches a short message from OpenAI (ChatGPT)
- Sends the message to a phone number that you define
- Can be configured to run at system startup on Linux

## How to Use

1. Clone this repository:

   git clone https://github.com/icybercaffe/whatsapp-automation.git
   cd whatsapp-automation

2. Create a virtual environment and install the requirements:

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Create a .env file in the project folder with the following:

   OPENAI_API_KEY=your_openai_key
   PHONE_NUMBER=your_phone_number
   SESSION_PATH=/full/path/to/whatsapp_session

4. Run the script manually to test:

   python3 send_whatsapp_selenium.py

5. (Optional) To run the script automatically at startup:
   - Create a .desktop file in ~/.config/autostart
   - Make sure your start_script.sh is executable

This project avoids committing sensitive data by using environment variables and a .gitignore file.
