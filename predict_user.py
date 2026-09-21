import tkinter as tk
import time
import joblib


MODEL_FILE = "keystroke_model.pkl"

TARGET_TEXT = "cyber security"

key_data = []
start_time = None


# Load trained model
model = joblib.load(MODEL_FILE)


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

    for item in reversed(key_data):

        if (
            item["key"] == event.keysym
            and "release_time" not in item
        ):

            item["release_time"] = release_time

            item["dwell_time"] = (
                release_time
                - item["press_time"]
            )

            break


def predict_user():
    global key_data, start_time

    text = text_entry.get()

    if text != TARGET_TEXT:

        result_label.config(
            text="Please type the correct sentence."
        )

        return

    valid_keys = [
        item
        for item in key_data
        if "dwell_time" in item
    ]

    if len(valid_keys) < 2:

        result_label.config(
            text="Not enough typing data."
        )

        return


    # Total typing time
    total_time = (
        valid_keys[-1]["release_time"]
        - valid_keys[0]["press_time"]
    )


    # Typing speed
    typing_speed = (
        len(TARGET_TEXT)
        / total_time
    )


    # Average dwell
    avg_dwell = sum(
        item["dwell_time"]
        for item in valid_keys
    ) / len(valid_keys)


    # Flight times
    flight_times = []

    for i in range(1, len(valid_keys)):

        flight = (
            valid_keys[i]["press_time"]
            - valid_keys[i - 1]["release_time"]
        )

        if flight >= 0:
            flight_times.append(flight)


    if flight_times:

        avg_flight = (
            sum(flight_times)
            / len(flight_times)
        )

    else:

        avg_flight = 0


    # Prediction
    sample = [[
        avg_dwell,
        avg_flight,
        typing_speed
    ]]


    prediction = model.predict(sample)

    predicted_user = prediction[0]


    # Probability
    probabilities = model.predict_proba(sample)[0]

    confidence = max(probabilities) * 100


    result_label.config(
        text=f"Predicted User: {predicted_user}\n"
             f"Confidence: {confidence:.2f}%"
    )


    # Reset
    key_data = []
    start_time = None
    text_entry.delete(0, tk.END)


# ---------------- GUI ----------------

window = tk.Tk()

window.title(
    "Keystroke User Recognition"
)

window.geometry("600x400")


title = tk.Label(
    window,
    text="KEYSTROKE USER RECOGNITION",
    font=("Arial", 18, "bold")
)

title.pack(pady=25)


instruction = tk.Label(
    window,
    text="Type the following sentence:",
    font=("Arial", 12)
)

instruction.pack()


sentence = tk.Label(
    window,
    text=TARGET_TEXT,
    font=("Arial", 16, "bold")
)

sentence.pack(pady=15)


text_entry = tk.Entry(
    window,
    width=40,
    font=("Arial", 14)
)

text_entry.pack(pady=20)


text_entry.bind(
    "<KeyPress>",
    key_press
)

text_entry.bind(
    "<KeyRelease>",
    key_release
)


predict_button = tk.Button(
    window,
    text="Recognize User",
    command=predict_user,
    width=20
)

predict_button.pack(pady=10)


result_label = tk.Label(
    window,
    text="",
    font=("Arial", 13),
    fg="blue"
)

result_label.pack(pady=20)


window.mainloop()