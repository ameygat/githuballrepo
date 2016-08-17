#Small Script to download all the repositories from a github organization
import sys,os,requests
giturl = "https://api.github.com/orgs/%s/repos?per_page=200"
if len(sys.argv) > 1:
    org = sys.argv[1]
    r = requests.get(giturl %(org))
    if r.status_code == 200:
        rdata = r.json()
	print "Got %d repositories for Organization: %s\nDownloading All!" % (len(rdata),org)
        for repo in rdata:
            os.system("git clone " + repo['clone_url'])
else:
    print "Usage: %s git_hub_org_name" % (sys.argv[0])