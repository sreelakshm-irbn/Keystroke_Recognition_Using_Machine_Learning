import tkinter as tk
import time
import csv
import os

DATA_FILE = "keystroke_data.csv"

# Text that every user must type
TARGET_TEXT = "cyber security"

# Store keystroke timings
key_data = []
start_time = None


def key_press(event):
    global start_time

    if start_time is None:
        start_time = time.perf_counter()

    key_data.append({
        "key": event.keysym,
        "press_time": time.perf_counter()
    })


def key_release(event):
    release_time = time.perf_counter()

    # Find the most recent matching key press
    for item in reversed(key_data):
        if item["key"] == event.keysym and "release_time" not in item:
            item["release_time"] = release_time
            item["dwell_time"] = (
                release_time - item["press_time"]
            )
            break


def save_data():
    global key_data, start_time

    user = user_entry.get().strip()

    if not user:
        status_label.config(text="Enter a user name.")
        return

    text = text_entry.get()

    if text != TARGET_TEXT:
        status_label.config(
            text="Please type the exact given sentence."
        )
        return

    valid_keys = [
        item for item in key_data
        if "dwell_time" in item
    ]

    if len(valid_keys) < 2:
        status_label.config(
            text="Not enough keystroke data."
        )
        return

    # Calculate total typing time
    total_time = (
        valid_keys[-1]["release_time"]
        - valid_keys[0]["press_time"]
    )

    # Typing speed
    typing_speed = len(TARGET_TEXT) / total_time

    # Average dwell time
    avg_dwell = sum(
        item["dwell_time"] for item in valid_keys
    ) / len(valid_keys)

    # Calculate flight times
    flight_times = []

    for i in range(1, len(valid_keys)):
        flight = (
            valid_keys[i]["press_time"]
            - valid_keys[i - 1]["release_time"]
        )

        if flight >= 0:
            flight_times.append(flight)

    if flight_times:
        avg_flight = sum(flight_times) / len(flight_times)
    else:
        avg_flight = 0

    # Save features
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "user",
                "avg_dwell_time",
                "avg_flight_time",
                "typing_speed"
            ])

        writer.writerow([
            user,
            avg_dwell,
            avg_flight,
            typing_speed
        ])

    status_label.config(
        text="Sample saved successfully!"
    )

    # Reset
    key_data = []
    start_time = None
    text_entry.delete(0, tk.END)


# ---------------- GUI ----------------

window = tk.Tk()
window.title("Keystroke Data Collection")
window.geometry("600x400")

title = tk.Label(
    window,
    text="KEYSTROKE DATA COLLECTION",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)

instruction = tk.Label(
    window,
    text="Type the following sentence exactly:",
    font=("Arial", 12)
)

instruction.pack()

sentence = tk.Label(
    window,
    text=TARGET_TEXT,
    font=("Arial", 16, "bold")
)

sentence.pack(pady=10)

user_label = tk.Label(
    window,
    text="User Name:"
)

user_label.pack()

user_entry = tk.Entry(
    window,
    width=30
)

user_entry.pack(pady=5)

text_entry = tk.Entry(
    window,
    width=40,
    font=("Arial", 14)
)

text_entry.pack(pady=20)

text_entry.bind("<KeyPress>", key_press)
text_entry.bind("<KeyRelease>", key_release)

save_button = tk.Button(
    window,
    text="Save Sample",
    command=save_data,
    width=20
)

save_button.pack(pady=10)

status_label = tk.Label(
    window,
    text="",
    fg="blue"
)

status_label.pack(pady=10)

window.mainloop()