# IP Recorder and Device Identifier
A Flask-based web application that records client IP addresses, device types, and device systems, along with their geographic locations (if allowed by the user).

## Features

* Records client IP addresses
* Identifies device types (Mobile, Desktop, or Bot)
* Identifies device systems (Windows, MacOS, Android, iOS, Linux, or Unknown)
* Records geographic locations (latitude and longitude) if allowed by the user
* Displays recorded results in a user-friendly format

## How to Use

1. Run the application by executing `python app.py` in your terminal.
2. Open a web browser and navigate to `http://localhost:5000/`.
3. The application will prompt you to allow or deny location access. Choose accordingly.
4. If you allow location access, the application will record your IP address, device type, device system, and geographic location.
5. If you deny location access, the application will still record your IP address, device type, and device system, but will indicate that the location is blocked.
6. To view the recorded results, navigate to `http://localhost:5000/result`.

## Technical Details

* The application uses Flask as the web framework.
* It uses the `request` object to get the client's IP address and user agent.
* It uses regular expressions to identify device types and systems from the user agent string.
* It uses the `datetime` module to record the current time.
* It stores the recorded results in a text file named `result.txt`.
* It uses templates to render the user interface.

## Live app 
* Join `https://khaledxab.pythonanywhere.com`
* You can find the ip result here `https://khaledxab.pythonanywhere.com/result`