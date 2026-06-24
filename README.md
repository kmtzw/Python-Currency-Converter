Global Currency Converter 💱

A dynamic, animated graphical user interface (GUI) application built in Python that provides real-time currency conversion for over 160 global currencies.

✨ Features

Real-Time Exchange Rates: Fetches live, up-to-date conversion rates via the ExchangeRate-API.

Extensive Currency Support: Convert between more than 160 different global currencies.

Animated UI: Features a custom animated processing ring and a sleek, modern dark-mode aesthetic.

Non-Blocking Operations: Uses multi-threading to fetch API data in the background without freezing the interface.

🛠️ Technologies Used

Python 3.x

Tkinter: Standard Python interface to the Tk GUI toolkit.

Requests: Elegant and simple HTTP library for Python used to fetch API data.

🚀 Getting Started

Prerequisites

Make sure you have Python installed on your computer. You will also need to install the requests library.

Installation & Setup

Clone the repository:

git clone [https://github.com/YOUR-USERNAME/python-currency-converter.git](https://github.com/YOUR-USERNAME/python-currency-converter.git)
cd python-currency-converter


Set up a virtual environment (Optional but recommended):

Windows: python -m venv venv followed by venv\Scripts\activate

macOS/Linux: python3 -m venv venv followed by source venv/bin/activate

Install the required dependencies:

pip install requests


💻 Usage

Run the application from your terminal:

python app.py


(Note: Use python3 app.py if you are on macOS or Linux).

Once the application opens:

Enter the amount you wish to convert.

Select your base currency from the "From" dropdown.

Select your target currency from the "To" dropdown.

Click Convert Rates and enjoy the animation!

📡 API Reference

This project uses the free ExchangeRate-API endpoint to retrieve live cross-rates. No authentication key is required for the basic endpoint used in this project.