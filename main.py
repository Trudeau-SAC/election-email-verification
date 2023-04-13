import os

# Get verified emails
verified_emails_file = open("data/verified_emails.txt", "r")
verified_emails = verified_emails_file.read().splitlines()

# Get voter emails
voter_emails_file = open("data/voter_emails.txt", "r")
voter_emails = voter_emails_file.read().splitlines()

# Get votes
votes_file = open("data/votes.txt")
votes = votes_file.read().splitlines()

# Remove duplicates and unverified emails
# If duplicate, first vote is used
new_voter_emails = []
new_votes = []
for i in range(len(voter_emails)):
    if voter_emails[i] in verified_emails and voter_emails[i] not in new_voter_emails:
        new_voter_emails.append(voter_emails[i])
        new_votes.append(votes[i])

# Create dictionary of candidates and votes
votes_dict = {}
for i in range(len(new_votes)):
    if new_votes[i] in votes_dict:
        votes_dict[new_votes[i]].append(new_voter_emails[i])
    else:
        votes_dict[new_votes[i]] = [new_voter_emails[i]]

# Sort candidates by number of votes
votes_dict = dict(sorted(votes_dict.items(), key=lambda item: len(item[1])))

# Print list of voters for each candidate
for candidate in votes_dict:
    print('People who voted for ' + candidate + ':')
    for voter in votes_dict[candidate]:
        print(voter)
    print()

# Print number of votes for each candidate
for candidate in votes_dict:
    print(candidate + ' has ' + str(len(votes_dict[candidate])) + ' votes!')
