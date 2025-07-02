# Raspberry Pi Always-On Dashboard Project

## What you have
- Raspberry Pi Zero 2 W (running Raspberry Pi OS Lite or similar)
- 5.5” 1920×1080 AMOLED over USB-C driver board
- 3 macro keys on XIAO RP2040
- Home Assistant on the same Pi
- Data to display: clock, timer, weather, calendar, Spotify info, Home Assistant telemetry

## Goal
Create a clean always-on dashboard UI with a retro aesthetic.  
Macro keys trigger Home Assistant automations (e.g., desk up/down, toggle lights).  
Local, lightweight, runs headless on Pi.  
Easy to add or modify widgets in the future.

---

## Step 1: System Setup

### OS & Dependencies  
Install Raspberry Pi OS Lite (Bookworm) (no desktop needed; keeps it lightweight).  

Install required packages:  
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv git
