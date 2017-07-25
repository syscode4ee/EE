import requests
import time
import pickle


def save_file_list(account, filelist, cachefiledir='state'):
        """Restre seen list from disk."""
        cachefile = cachefiledir + '/' + account + '_cache.p'
        pickle.dump(filelist, open(cachefile, "wb"))


def load_file_list(account, cachefiledir='state'):
        """Dump seen list to disk."""
        cachefile = cachefiledir + '/' + account + '_cache.p'
        return pickle.load(open(cachefile, "rb"))


def get_gists(account):
        """Do a HTTP gist request."""
        url = "https://api.github.com/users/%s/gists" % account
        result = requests.get(url)
        blob = result.json()
        files = list()
        for gist in blob:
            if 'files' in gist:
                files += list(gist['files'].keys())
        if len(files) == 0:
            print "no public gists found for %s" % account
        else:
            print ("currently %d public gists in %s github: %s" % (
                len(files), account, ', '.join(files)))
        return files


def push_gist(token):
        """Push a gist."""
        url = "https://api.github.com/gists"
        headers = {'Authorization': 'token %s' % token}
        params = {'scope': 'gist'}
        ts = time.strftime('%Y%m%d%H%M%S')
        filename = "demogist-%s.txt" % ts
        description = "this is a demo gist"
        data = """{
        "description": "%s",
        "public": "true",
        "files": {
          "%s": {
            "content": "demo gist. timestamp is %s"
          }
        }
        }"""
        json_data = data % (description, filename, ts)
        result = requests.post(
            url,
            headers=headers,
            params=params,
            data=json_data
        )
        result_url = result.json()['files'][filename]['raw_url']
        print "pushed new gist at %s" % result_url


def checkgists(account):
    """Check current public gists and notify if new ones are present."""
    oldlist = set()
    try:
        oldlist = set(load_file_list(account))
    except:
        pass
    newlist = set(get_gists(account))
    save_file_list(account, newlist)

    diff = newlist - oldlist
    if len(diff) > 0:
        print ("new public gists found! %s" % ', '.join(diff))
