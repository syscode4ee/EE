#!/usr/bin/env python

import gistlib as gist
import time

# this needs to be a personal access token with 'gist' permission
token = '883b49ccae5d11094115298dd6703065e03f34eb'
account = 'syscode4ee'

gist.checkgists(account)
time.sleep(5)
gist.push_gist(token)
time.sleep(5)
gist.checkgists(account)
