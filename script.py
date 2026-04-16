import requests
from datetime import datetime

LOG_FILE = "website-health.log"


def get_timestamp():
    """Return current timestamp in readable format"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_message(message):
    """Append message to log file with timestamp"""
    with open(LOG_FILE, "a") as f:
        f.write(f"{get_timestamp()} - {message}\n")


def check_website(url):
    """Check if a website is up or down"""
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        if status_code == 200:
            log_message(f"{url} is UP (Status: {status_code})")
        else:
            log_message(f"{url} is DOWN (Status: {status_code})")

    except requests.exceptions.RequestException as e:
        log_message(f"{url} is DOWN (Error: {str(e)})")


def main():
    url = "https://google.com"
    check_website(url)


if __name__ == "__main__":
    main()