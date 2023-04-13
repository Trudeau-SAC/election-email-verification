# election-email-verification

Tallys up electronic student election votes while ensuring no duplicates and no unauthorized voters.
If duplicates are found, only the first vote is used.

## How to Use
1. Paste the following information from your spreadsheet into the text files in `/data`, one entry per line
   - `verified_emails.txt`: Emails of students who are allowed to vote
   - `voter_emails.txt`: Emails of voters
   - `votes.txt`: Choices of voters, each corresponding to an email in `voter_emails.txt`
2. `python3 main.py`
