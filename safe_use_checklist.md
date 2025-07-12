## GitHub Copilot Pilot: Governance & Safe Use Checklist

### Data Privacy & IP Protection
- Never paste sensitive code or credentials into prompts.
- Disable "public code suggestions" unless team agrees.
- Review org-wide Copilot settings in GitHub Enterprise admin.

### Safe Experimentation Practices
- Start in non-prod codebases or sandbox repos.
- Tag all Copilot-assisted commits (`[copilot]` in commit message).
- Enable code review for all AI-assisted changes.

### Good Prompt Hygiene
- Keep comments concise and context-rich.
- Ask explicitly: `# Write a function to...` yields better results.
- Avoid overloading Copilot with ambiguous or legacy code.

### Governance & Auditing
- Track where Copilot is being used and by whom.
- Introduce a monthly feedback retro: “What did Copilot help/hurt?”
- Document all generated code as AI-assisted.

### Safe Defaults for Pilot Phase
- Pilot in shared test repos.
- Assign Copilot champions in each squad.
- Review and record lessons monthly.
