## GitHub Copilot Pilot: Governance & Safe Use Checklist

### Prompting with Sensitive Information

Avoid including sensitive data in your prompts, e.g. production secrets (passwords/API keys/etc), IP addresses, customer identifiers, etc.

Examples of bad prompts:
- Using this API key: sk_live_ABC123 check our payment service health
- Connect to internal database at 10.45.66.20 using service account `prod_user`
- Use my github account user123/passwordxyz to create a new repository and commit the workspace
- Write a function to fetch NVIDIA stock price every 5 mins from Yahoo Finance using API key e4d909c290d0fb1ca068ffaddf22cbd0
- Given these 10 customers transaction history write a program that detects anomalies.

Instead you can use fake names as wildcards that you can replace as necessary.
- Write a python function that scrapes the intranet site intranet.mycompany.com once everyday and detect new articles.

It is tempting to use the Ask mode to ask questions that will not persist in the workspace, but remember that your prompts can reside with the model.

### Copyrights or Licenses of Copilot-Suggested Code

Copilot isn’t always clear about where code comes from. That’s why governance and review processes still matter — especially in financial services

- Sometimes after Copilot has completed a task you could see a line like this:
    "Similar code found with (n) license types - View matches"

- For example you are very likely to get this if you give a prompt like:
    "implement sha256 in python"

- When this happens you need to make sure that the cited license allows you to use the code for your intended purpose.

- Creative Commons Zero (CC0) is probably the most permissive license type, followed by MIT license which allows you to freely use and change the code but requires attribution.

- Avoid GPL/AGPL/LGPL as these are "copyleft" licenses that require sharing source code and derivative works under the same license.

- Seek internal guidelines on what license types are permitted. 

### Unsafe Defaults or Incomplete Security

Copilot suggests things based on training data, not security awareness. It will not necessarily always know what's safe.

Example of a bad prompt:
    "send an API key in a GET request to authenticate"

To which Copilot might respond with:
    "url = f"https://api.example.com?apikey={API_KEY}""

You should:

- Always review authentication logic

- Use POST over GET for credentials

- Lint/check Copilot output for OWASP risks

### Overtrust in Copilot Logic

Copilot generates confident code — even when it’s wrong. That’s why reviews and test coverage are still required.

You might use a prompt like: "write retry logic with exponential backoff" and Copilot might respond with code that looks great but missing a sleep timer.

- Don't skip tests or manual review just because code is AI-generated.

- Copilot is a developer, not a solution designer nor a senior architect.

### Governance in Practice

We don't just adopt Copilot — we govern its use. That starts with awareness and habits, not just policy documents.

Examples to consider:

- Tag AI-assisted commits: [copilot]

- Add comments: # this was suggested by Copilot

- Periodic retros: “Where did Copilot help or mislead us?”


