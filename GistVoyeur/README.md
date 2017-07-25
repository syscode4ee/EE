# Tool to query the Github API for new gists

## exercise
**Github API**
Using the Github API you should query a user’s publicly available github gists. The script should then tell you when a new gist has been published.

## assumptions
I have taken the route of creating my own tool and lib, called 'Gist Voyeur' :D
The tool will require the `requests` python module. I suggest to install it in
a virtualenv to avoid messing up with system library

I use OSX for the test and python 2.7.


## scripted solution

### requirements
```
cd GistVoyeur
sudo easy_install virtualenv
virtualenv gistdemo
source gistdemo/bin/activate
pip install requests
```

### check new gists

the script contains a variable `account` that needs to be updated with the github account of your choice (the one you want to check gists for)

```
python voyeur.py
```
if, in the meanwhile you add a Gist to your account (ie, from the browser) and rerun the program, it will notify it.

the script uses a 'state' file per account, in the example under the 'state'  local directory.

### test the pipeline (check-add-check)

(you may want to use another account than the one in the demo, please update the token variable)
```
python voyeur-with-push.py
```
This companion script will demonstrate before and after a gist add.

Sometimes accounts hitting the  github api get 'flagged' for suspicious activity. If you abuse this script it can happen as well.

## improvements
This can be easily wrapped up into packer to create a ready to use vagrant box.
Also, this is a very basic jenkins install (rather than blueocean), for example it could benefit from scm checkout (backups) or shared storage for HA.
