from datetime import datetime
import requests


def generate_log(data):
    """
    Write a list of log entries to a timestamped text file in the
    current working directory.

    Args:
        data (list): A list of strings, each a log entry. An empty
                      list is valid and produces an empty log file.

    Returns:
        str: The generated filename (e.g. "log_20260831.txt").

    Raises:
        ValueError: If data is not a list.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list of strings.")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    """
    Fetch a sample post from the JSONPlaceholder API.
    Returns the JSON response as a dict, or an empty dict on failure.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    # Example: generate a log file
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)

    # Example: fetch data from the API
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    