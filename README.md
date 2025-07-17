This project is created to demonstrate the usage of Github Copilot through a real life use-case.

It's a CLI tool to check online status for a given url. It relies on a third-party API from the RapidAPI.com marketplace to check if the given URL is reachable.

# Syntax
python healthcheck.py --url https://google.com

# Setup

- Clone the repository
git clone https://github.com/akram0zaki/GithubCopilotDemo.git

- Navigate to the project directory
cd GithubCopilotDemo

- (Optional) Create a virtual environment:
python -m venv .venv

- (Optional) Activate the virtual environment:
.\.venv\Scripts\activate    (for Windows)

- Install the dependencies:
pip install requests dotenv

# Dependencies

This demo application uses the API [instant-uptime-checker](https://rapidapi.com/daytrader803/api/instant-uptime-checker) from the RapidAPI.com marketplace.

To be able to use it you need to sign up to the free plan of [rapidapi.com](https://rapidapi.com/auth/sign-up)  and subscribe to the API.
You will need to place your RAPID API KEY in the .env file.

