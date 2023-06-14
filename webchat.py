import requests
import ctypes

url = 'https://webchat.quakenet.org/'

# Set the text color to green
ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 10)

channel = input("Enter channel name (optional): ")
if channel:
    url += '?channels=' + channel

response = requests.get(url)

if response.status_code == 200:
    print('Successfully connected to QuakeNet web chat.')
    print('URL:', response.url)
else:
    print('Failed to connect to QuakeNet web chat.')

# Reset the text color to the default
ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 7)
