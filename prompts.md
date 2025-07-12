
# Prompts for Copilot

# Setup and Documentation
- create a .gitignore file for this project
- create a requirements.txt file
- create a user guide for this project explaining how to set it up and how to run it

## Functionality
- write a function that checks multiple URLs in parallel using threads
- write retry logic for check_website_uptime with exponential backoff
- load a list of URLs from a file and check each one
- support a --config argument to read API key from JSON or .env
- implement --slack flag to send alerts via Slack webhook

# Usability
- add color-coded output for status: green for OK, red for errors
- print a summary line at the end: X services up, Y down
- log to a file if --log flag is provided

## Testing and Quality
- write a test for check_website_uptime using unittest and mock
- write unit tests for the CLI using pytest

## Refactoring and Improvements
- refactor this to use async/await with aiohttp
- move API config into a separate module
- extract logging setup into reusable function

## For Ask mode:
- what happens if the API returns an unexpected format?
- write docstring for this function
