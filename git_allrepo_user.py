#Small Script to download all the repositories from a github user
import sys,os,requests
giturl = "https://api.github.com/users/%s/repos?per_page=200"
if len(sys.argv) > 1:
    user = sys.argv[1]
    r = requests.get(giturl %(user))
    if r.status_code == 200:
        rdata = r.json()
	print "Got %d repositories for user %s\nDownloading All!" % (len(rdata),user)
        for repo in rdata:
            os.system("git clone " + repo['clone_url'])
else:
    print "Usage: %s git_hub_username" % (sys.argv[0])