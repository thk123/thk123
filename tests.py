import glob, os
import re
def checkEmails():
	for file_path in glob.glob("*.html"):
		with open(file_path, 'r') as f:
			for line in f:
				m = re.search("mailto:(.*@.*)\">(.*@.*)</a>", line)
				if m:
					print("Found email:" + m.group(1))

					if(m.group(1) != "hi@tkiley.co.uk"):
						print("Error: invalid email link in " + file_path + ": " + m.group(1))

					if(m.group(2) != "hi@tkiley.co.uk"):
						print("Error: invalid email text in " + file_path + ": " + m.group(2))




checkEmails()
