import asyncio
import threading
import tkinter as tk


from toyControl import *

background_loop = None #background events loop


def start_async_loop():
    global background_loop
    background_loop = asyncio.new_event_loop()
    # set_event_loop tells this specific thread to use this loop
    asyncio.set_event_loop(background_loop)
    # run_forever keeps the thread alive, waiting for work
    background_loop.run_forever()

def on_test_vibrate_button_click(btn):
    # Change the text property of the button dynamically
    btn.configure(state="disabled")
    if background_loop and background_loop.is_running():
        # Safely submit the async coroutine to the running background loop.
        # This returns instantly, meaning your GUI never freezes!
        asyncio.run_coroutine_threadsafe(
            vibeAtPowerExperiment(0.5), background_loop
        )

    else:
        print("Error: Background loop is not running.")
    btn.configure(state="active")

def client_start(request_btn, control_btn):
    request_btn.configure(state="disabled")
    if background_loop and background_loop.is_running():
        # Safely submit the async coroutine to the running background loop.
        # This returns instantly, meaning your GUI never freezes!
        print("Starting Client...")
        asyncio.run_coroutine_threadsafe(
            initialiseClient(), background_loop
        )
        print("Client Start Requested")

    else:
        print("Error: Background loop is not running.")

    control_btn.configure(text="Starting server")
    control_btn.configure(state="active")

def stop_devices_button():

    if background_loop and background_loop.is_running():
        # Safely submit the async coroutine to the running background loop.
        # This returns instantly, meaning your GUI never freezes!
        print("Starting Client...")
        asyncio.run_coroutine_threadsafe(
            stopDevices(), background_loop
        )
        print("Client Start Requested")

    else:
        print("Error: Background loop is not running.")


def main():
    print("Application Started")
    print("""
========================================================
Welcome to the Motivation Software graphical interface!

    This is the interface for "motivation" in your 
    coding activities!
    
========================================================
""")
    root = tk.Tk()
    root.geometry("500x700")

    # The button triggers the synchronous wrapper function
    request_client_btn = tk.Button(root, text="Start", state="active",
                                 command=lambda: client_start(request_client_btn, test_vibrate_btn))


    # The button triggers the synchronous wrapper function too
    test_vibrate_btn = tk.Button(root, text="press start", state="disabled",
                                 command=lambda: on_test_vibrate_button_click(test_vibrate_btn))

    off_vibrate_btn = tk.Button(root, text="stop devices", state="active",
                                command=lambda: stop_devices_button())

    quit_button = tk.Button(root, text="Exit", command=root.destroy)

    request_client_btn.pack(pady=1)
    test_vibrate_btn.pack(pady=1)
    off_vibrate_btn.pack(pady=1)
    quit_button.pack(pady=1)






    threading.Thread(target=start_async_loop, daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    main()
