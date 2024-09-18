# Developer: Amruth Gudigar <amruthgudigar111@gmail.com>
# Date: 18-09-2024
# Description: SINR Prediction Calculator

import tkinter as tk
from math import log10

def calculate_sinr():
    try:
        rx_power = float(rx_power_entry.get())
        interference_power = float(interference_power_entry.get())
        bandwidth = float(bandwidth_entry.get())
        k = 1.38e-23
        T = 300
        bandwidth = bandwidth * 1e6
        noise_power = k * T * bandwidth * 1e3
        snr_dB = rx_power - 10 * log10(noise_power)
        sinr_dB = rx_power - 10 * log10(noise_power + 10**(interference_power/10))
        sinr_output.config(text=f"SNR: {snr_dB:.2f} dB\nSINR: {sinr_dB:.2f} dB")
    except ValueError:
        sinr_output.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("SINR Pediction Calculator")
root.geometry("310x300")  # Set the window size to 300x250

# Create and place widgets
rx_power_label = tk.Label(root, text="Enter RX Power (dBm)", font=("Arial", 10))
rx_power_label.pack(pady=10)

rx_power_entry = tk.Entry(root, font=("Arial", 10))
rx_power_entry.pack()

interference_power_label = tk.Label(root, text="Enter Interference Power (dBm)", font=("Arial", 10))
interference_power_label.pack(pady=10)

interference_power_entry = tk.Entry(root, font=("Arial", 10))
interference_power_entry.pack()

bandwidth_label = tk.Label(root, text="Enter Bandwidth (MHz)", font=("Arial", 10))
bandwidth_label.pack(pady=10)

bandwidth_entry = tk.Entry(root, font=("Arial", 10))
bandwidth_entry.pack()

calculate_button = tk.Button(root, text="Calculate SINR", command=calculate_sinr, font=("Arial", 10))
calculate_button.pack(pady=10)

sinr_output = tk.Label(root, text="", font=("Arial", 16, "bold"))
sinr_output.pack()

root.mainloop()