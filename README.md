# Brute-Force
OTP Brute Force Script
Overview
This Python script brute-forces a 4-digit OTP (0000–9999) on a web application requiring OTP verification. It uses multithreading to attempt multiple OTPs simultaneously.

Requirements
Python 3.x
requests library: pip install requests
Usage
Clone or download the script.

Run the script:

bash
Copy
Edit
python otp_brute_force.py
Input the following when prompted:

IP address (e.g., 10.10.84.173)
URL (e.g., /reset_password.php)
Email (e.g., tester@hammer.thm)
The script will attempt all 4-digit OTP combinations.

How It Works
Multithreading: Uses multiple threads to speed up the brute-forcing process.
Requests: Sends POST requests to submit OTPs.
Success: The script checks for a success indicator (e.g., 'Success' in the response text).
Example
yaml
Copy
Edit
Enter the IP address: 10.10.84.173
Enter the target URL: /reset_password.php
Enter the email address: tester@hammer.thm
Trying OTP: 0000 - Status Code: 200
Trying OTP: 1234 - Status Code: 200
OTP Found: 1234
Notes
Rate Limiting: May be triggered by some applications.
Legality: Use only on systems you have explicit permission to test.
