#!/bin/bash
sleep 30
source "$HOME/whatsapp_automation/venv/bin/activate"
python3 "$HOME/whatsapp_automation/send_whatsapp_selenium.py" >> "$HOME/whatsapp_automation/autostart.log" 2>&1

