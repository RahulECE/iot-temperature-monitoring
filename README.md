# IoT Device-Server Communication Project

## Project Overview

This project implements a simple IoT system where a device sends temperature data to a server. The communication is done using **Flask** (a lightweight Python web framework) on the server-side and **HTTP requests** on the device-side. The server receives temperature data and logs it, while the device continuously sends simulated temperature readings.

### Components:
- **Server**: Listens for incoming temperature data via HTTP POST requests and logs it.
- **Device**: Sends random temperature data to the server at regular intervals.

## Project Structure

IoT │ ├── venv/ # Virtual environment for dependencies ├── server.py # Flask server to handle data from IoT device ├── device.py # Simulated device sending random temperature data ├── .gitignore # Specifies files and directories to ignore in Git ├── README.md # Project description and instructions └── requirements.txt # Python dependencies for the project


## How to Run the Project

### Step 1: Set up the Virtual Environment

Before running the project, it’s a good practice to use a virtual environment to manage dependencies. To create and activate the virtual environment:

```
cd /path/to/project/IoT
python3 -m venv venv
source venv/bin/activate   # Linux or Mac
# For Windows: venv\Scripts\activate
```
Step 2: Install Dependencies
Once the virtual environment is active, install the required Python packages by running:
```
pip install -r requirements.txt
```
Step 3: Running the Flask Server
To start the Flask server, run the following command inside the project directory
```
python3 server.py
```
This will start the Flask server on http://127.0.0.1:5000 and it will listen for incoming POST requests from the device.

Step 4: Running the IoT Device Simulation
In another terminal window, activate the virtual environment again and run the device simulation:

```
cd /path/to/project/IoT
source venv/bin/activate   # Activate virtual environment
python3 device.py
```
This will start sending random temperature data from the device to the server.

Code Description
server.py
The server.py file contains the Flask-based server code. It listens on the /data endpoint for incoming POST requests containing temperature data.
device.py
The device.py file simulates a device that sends random temperature data to the Flask server at regular intervals.
Step 5: Deactivate the Virtual Environment (optional)
After finishing, you can deactivate the virtual environment by running:
```
deactivate
```
