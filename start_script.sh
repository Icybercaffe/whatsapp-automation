#!/bin/bash
sleep 30
source /home/trendy/whatsapp_automation/venv/bin/activate
python3 /home/trendy/whatsapp_automation/send_whatsapp_selenium.py >> /home/trendy/whatsapp_automation/autostart.log 2>&1
