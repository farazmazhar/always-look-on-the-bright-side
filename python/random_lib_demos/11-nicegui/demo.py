"""
nicegui demo — build a small web UI in pure Python.

Run with:  .venv/bin/python 11-nicegui/demo.py

This starts a local web server. Open the URL printed in the terminal
(http://localhost:8080) in a browser, play with the widgets, then press
Ctrl+C to stop.

Everything below is Python: the UI elements, their event handlers, and a
background timer that pushes live updates to the browser.
"""

from datetime import datetime

from nicegui import ui


# ---------------------------------------------------------------------------
# 1. The page
# ---------------------------------------------------------------------------
@ui.page("/")  # this Python function becomes the home page
def index():
    # --- a heading and a live "clock" label updated by a timer ---
    ui.label("NiceGUI demo").classes("text-2xl font-bold")

    clock = ui.label("waiting for first tick...")
    ui.timer(1.0, lambda: clock.set_text(f"Server time: {datetime.now():%H:%M:%S}"))

    # --- a counter button: state lives in a closure, no JS needed ---
    ui.markdown("### Counter")
    counter = ui.label("0").classes("text-3xl")

    def bump():
        counter.set_text(str(int(counter.text) + 1))

    ui.button("+1", on_click=bump)

    # --- a slider that drives a computed value live ---
    ui.markdown("### Temperature converter")
    celsius = ui.slider(min=-20, max=50, value=20).classes("w-64")
    fahrenheit = ui.label()

    def update_fahrenheit(e):
        f = e.value * 9 / 5 + 32
        fahrenheit.set_text(f"{e.value} °C = {f:.1f} °F")

    celsius.on_value_change(update_fahrenheit)
    update_fahrenheit(type("E", (), {"value": 20})())  # prime the label

    # --- a select dropdown + notification ---
    ui.markdown("### Choose a fruit")
    fruit = ui.select(["apple", "banana", "cherry"], value="apple")

    def on_pick():
        ui.notify(f"You picked {fruit.value}!", type="positive")

    ui.button("Confirm", on_click=on_pick)

    # --- text input with a live greeting ---
    ui.markdown("### Say hello")
    name = ui.input("Your name", placeholder="type here...")
    greeting = ui.label()

    name.on_value_change(lambda e: greeting.set_text(f"Hello, {e.value or 'stranger'}!"))


# ---------------------------------------------------------------------------
# 2. Start the server
# ---------------------------------------------------------------------------
# show=False: do NOT auto-open a browser (useful on headless servers/remotes).
# Just visit http://localhost:8080 yourself.
ui.run(host="0.0.0.0", port=8080, show=False, title="NiceGUI Demo")
