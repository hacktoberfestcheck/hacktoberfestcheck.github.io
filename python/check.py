import urllib.request
import datetime
import json
import sys

if len(sys.argv)!=1:
    url = sys.argv[1]
else:
    url = input("Enter a valid GitHub url: ")

if url.startswith("https://github.com/"):

    urltopics = (url.replace("github.com", "api.github.com/repos") + "/topics").replace("//topic", "/topic")

    rawtopics = urllib.request.urlopen(urltopics).read()

    topics = json.loads(rawtopics)["names"]

    urllabels = (url.replace("github.com", "api.github.com/repos") + "/labels/hacktoberfest-accepted").replace("//labels", "/labels")

    # Checks if Hacktoberfest is in the Topics list.
    topicsresult = ("hacktoberfest" in topics)

    labelsresult = True

    # Check if label exists via 404 error code.
    try:
        urllib.request.urlopen(urllabels)
    except:
        labelsresult = False

    if datetime.date.today().month<10:
        print("Hacktoberfest hasn't started yet.")
    if datetime.date.today().month>10:
        print("Hacktoberfest has ended, but you can wait till next year!")
    elif topicsresult:
        print("This repo is opted into Hacktoberfest! (via Topics)")
    elif labelsresult:
        print("This repo is opted into Hacktoberfest! (via Labels)")
    else:
        print("Unfortunately, this repository is not opted into Hacktoberfest.")

elif url.startswith("https://hacktoberfest.digitalocean.com"):
    print("That's the Hacktoberfest website!")
else:
    print("That is not a valid GitHub repository!")