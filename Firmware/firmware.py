# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃   Raspberry Pi Zero 2 W Macropad Dashboard Companion      ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# 🎯 GOAL:
# Create a lightweight, local dashboard (retro-themed) displayed via Chromium kiosk mode,
# controlled partially via macro keys running KMK firmware on XIAO RP2040.
# Macro keys send USB HID keycodes (e.g., F17, F18, F19), which the Raspberry Pi listens for.
# Each key triggers Home Assistant automations such as desk height control and lights.

# 🧱 STACK OVERVIEW:
# ─ Raspberry Pi OS Lite (Bookworm) on Pi Zero 2 W
# ─ Home Assistant Core (on same Pi)
# ─ Flask backend to serve dashboard API (/api/weather, /api/spotify, etc.)
# ─ Chromium in kiosk mode (dashboard in fullscreen browser)
# ─ KMK firmware on XIAO RP2040 (USB HID macropad)
# ─ Retro aesthetic HTML/CSS dashboard frontend

# 🧩 Each macro key mapped to:
# ─ KC.F17 → Home Assistant automation: Desk Up
# ─ KC.F18 → Home Assistant automation: Desk Down
# ─ KC.F19 → Toggle Light or Scene

# 📍 Macro key detection:
# On the Pi, use either:
# (A) Home Assistant “Keyboard” integration to capture keypresses (F17–F19), or
# (B) Python script using `evdev` to listen for `/dev/input/event*` and trigger automations via Home Assistant REST API.

# 🔁 Future features:
# ─ Real-time sensor widgets (desk height, temp, etc.) via ESPHome or MQTT
# ─ Custom widget framework to modify/add dashboard panels easily
# ─ Optional theme switching (night/day mode)
# ─ Timer controls via another keypress or frontend

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                KMK CODE                 ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# Import physical board pin mappings
import board

# KMK core modules
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Create keyboard object instance
keyboard = KMKKeyboard()

# Enable macros (not used directly here, but ready for future use)
macros = Macros()
keyboard.modules.append(macros)

# Define physical pins connected to buttons
# Match your wiring: D4, D2, D1
PINS = [board.D4, board.D2, board.D1]

# Setup key scanner (not a matrix, just direct pin reads)
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # Adjust if needed
)

# Keymap:
# Assign keys to uncommon function keys (F17-F19) to avoid conflict with regular use
# These will be captured by the Pi to trigger automations in Home Assistant
keyboard.keymap = [
    [KC.F17, KC.F18, KC.F19]
    # ⬆ F17 → Desk Up
    # ⬆ F18 → Desk Down
    # ⬆ F19 → Toggle Lights
]

# Start the KMK firmware loop
if __name__ == '__main__':
    keyboard.go()
