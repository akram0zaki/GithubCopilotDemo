# Copilot AI Coding Agent Instructions for GithubCopilotDemo

## Project Overview
- This is a CLI tool for checking the online status of a given URL using a third-party API (RapidAPI instant-uptime-checker).
- Main entry point: `healthcheck.py`.
- API key is required and must be placed in a `.env` file (never hardcoded).

## Architecture & Data Flow
- User runs: `python healthcheck.py --url <target_url>`
- The script loads the API key from environment variables using `dotenv`.
- It sends a request to the RapidAPI endpoint to check the status of the provided URL.
- All network requests must use HTTPS.
- Sensitive data (API keys) must be loaded from environment variables, not committed to source control.

## Developer Workflows
- **Setup:**
  - Create and activate a Python virtual environment: `python -m venv .venv` and `source .venv/bin/activate` (or `./.venv/Scripts/activate.ps1` on Windows).
  - Install dependencies: `pip install requests dotenv`
- **Run:**
  - `python healthcheck.py --url https://example.com`
- **Test:**
  - (Add tests in a `tests/` directory if expanding the project.)
- **Secrets:**
  - Store API keys in `.env` (never hardcoded). Example: `RAPIDAPI_KEY=...`
  - `.env` is excluded via `.gitignore`.

## Security & Conventions
- Follows OWASP secure coding guidelines (see `.github/instructions/owasp.instructions.md`).
- All outbound URLs must be validated against an allow-list to prevent SSRF.
- Never log or expose secrets in error messages or output.
- Use parameterized queries and context-aware encoding if expanding to database or frontend code.

## Integration Points
- External dependency: RapidAPI instant-uptime-checker (see README for setup).
- Uses `requests` for HTTP and `dotenv` for environment variable management.

## Key Files & Patterns
- `healthcheck.py`: Main CLI logic and API integration.
- `.env.example`: Template for required environment variables.
- `.gitignore`: Excludes `.env`, virtual environment, and other sensitive files.
- `.github/instructions/owasp.instructions.md`: Security requirements for all code.
- `README.md`: Setup, usage, and dependency instructions.

## Example Usage
```sh
python healthcheck.py --url https://google.com
```

## For AI Agents
- Always validate URLs and never trust user input blindly.
- Never commit secrets or sensitive data.
- Reference `.github/instructions/owasp.instructions.md` for security requirements.
- If unsure about a workflow, check `README.md` for setup and usage details.
