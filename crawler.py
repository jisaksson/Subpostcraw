import praw

user_agent = "Subpostcraw v0.001 by JIsaksson"

print("Subpostcraw running!")

# connect to Reddit
r = praw.Reddit(user_agent)

# prompt for the username and subreddit you want to check
username = input('\nWhat is the username you would like to check? ')
sub = input("\nWhat is the subreddit you would like to crawl? ")

# get their redditor class
try:
	user = r.get_redditor(username)
except Exception as e:
	print("Something went wrong getting the user :(")
	raise
	
submitted = user.get_submitted(limit=None)

# begin checking submitted links
print("Checking submitted links...\n")
poster = False
cnt = 0
for link in submitted:
	subreddit = link.subreddit.display_name.lower()
	if subreddit == sub:
		print (link.title, "\n", link.url)
		poster = True
		cnt = cnt + 1

# print our result
if poster:
	print(username, "has submitted to ", sub, " ", cnt, "time(s)\n")
else:
	print(username, "has not submitted to ", sub, "\n")
