import tkinter as tk
from tkinter import ttk
import requests
import threading

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Currency Converter")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e")  # Dark modern theme

        # State variables
        self.rates = {}
        self.currencies = []
        self.animation_angle = 0
        self.is_animating = False

        self.setup_ui()
        # Fetch rates in a background thread to prevent GUI freezing
        threading.Thread(target=self.fetch_rates, daemon=True).start()

    def setup_ui(self):
        # Title Label
        title = tk.Label(self.root, text="Currency Converter", font=("Helvetica", 18, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        title.pack(pady=20)

        # Input Frame
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.pack(pady=10, padx=20, fill="x")

        # Amount Input
        tk.Label(frame, text="Amount:", fg="#bac2de", bg="#1e1e2e", font=("Helvetica", 11)).grid(row=0, column=0, sticky="w", pady=5)
        self.amount_entry = tk.Entry(frame, font=("Helvetica", 14), bg="#313244", fg="#cdd6f4", insertbackground="white", bd=0)
        self.amount_entry.insert(0, "100")
        self.amount_entry.grid(row=0, column=1, pady=5, sticky="ew")

        # From Currency
        tk.Label(frame, text="From:", fg="#bac2de", bg="#1e1e2e", font=("Helvetica", 11)).grid(row=1, column=0, sticky="w", pady=5)
        self.from_dropdown = ttk.Combobox(frame, font=("Helvetica", 12), state="readonly")
        self.from_dropdown.grid(row=1, column=1, pady=5, sticky="ew")

        # To Currency
        tk.Label(frame, text="To:", fg="#bac2de", bg="#1e1e2e", font=("Helvetica", 11)).grid(row=2, column=0, sticky="w", pady=5)
        self.to_dropdown = ttk.Combobox(frame, font=("Helvetica", 12), state="readonly")
        self.to_dropdown.grid(row=2, column=1, pady=5, sticky="ew")

        frame.columnconfigure(1, weight=1)

        # Animation Canvas
        self.canvas = tk.Canvas(self.root, width=100, height=100, bg="#1e1e2e", bd=0, highlightthickness=0)
        self.canvas.pack(pady=10)

        # Convert Button
        self.convert_btn = tk.Button(self.root, text="Convert Rates", font=("Helvetica", 12, "bold"), bg="#a6e3a1", fg="#11111b", activebackground="#94e2d5", bd=0, command=self.start_conversion_animation)
        self.convert_btn.pack(pady=10, ipady=5, ipadx=20)

        # Result Display
        self.result_label = tk.Label(self.root, text="Select currencies to begin", font=("Helvetica", 14), fg="#94e2d5", bg="#1e1e2e", wraplength=400)
        self.result_label.pack(pady=20)

    def fetch_rates(self):
        try:
            # Using standard free open API endpoint (Base USD)
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            data = response.json()
            if data["result"] == "success":
                self.rates = data["rates"]
                self.currencies = sorted(list(self.rates.keys()))
                
                # Update dropdown menus safely from background thread
                self.root.after(0, self.populate_dropdowns)
            else:
                self.root.after(0, lambda: self.result_label.config(text="Error loading rate data."))
        except Exception as e:
            self.root.after(0, lambda: self.result_label.config(text="Network error. Check connection."))

    def populate_dropdowns(self):
        self.from_dropdown['values'] = self.currencies
        self.to_dropdown['values'] = self.currencies
        
        # Set defaults if available
        if "USD" in self.currencies: self.from_dropdown.set("USD")
        if "EUR" in self.currencies: self.to_dropdown.set("EUR")

    def start_conversion_animation(self):
        if self.is_animating or not self.rates:
            return
        try:
            float(self.amount_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid numeric amount.")
            return

        self.is_animating = True
        self.animation_angle = 0
        self.animate_spinner()
        
        # Simulate processing time/calculation lag for dramatic effect
        self.root.after(1200, self.perform_calculation)

    def animate_spinner(self):
        if not self.is_animating:
            self.canvas.delete("all")
            return

        self.canvas.delete("all")
        # Draw a spinning futuristic arc circle
        self.canvas.create_arc(20, 20, 80, 80, start=self.animation_angle, extent=60, outline="#f38ba8", width=4)
        self.canvas.create_arc(20, 20, 80, 80, start=self.animation_angle + 180, extent=60, outline="#89b4fa", width=4)
        
        self.animation_angle = (self.animation_angle + 10) % 360
        self.root.after(20, self.animate_spinner)

    def perform_calculation(self):
        self.is_animating = False
        
        amount = float(self.amount_entry.get())
        from_curr = self.from_dropdown.get()
        to_curr = self.to_dropdown.get()

        # Conversion math using base USD cross multiplication
        # Standard logic: Amount * (Target Rate / Base Rate)
        usd_amount = amount / self.rates[from_curr]
        converted_amount = usd_amount * self.rates[to_curr]

        self.result_label.config(
            text=f"{amount:,.2f} {from_curr} =\n{converted_amount:,.2f} {to_curr}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()