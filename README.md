# Art Party Raffle script
A script to query Twitter for tagged images and randomly select a list of winners!

## Requirements
Python 3 environment

## How to use
No command arguments at the moment so you'll need to modify a couple variables to your liking.

* Change `tagname` to be your Art Party hashtag
* (Optional) Change `hostList` to include you and your cabal's usernames to avoid Nepotism!
* You'll need a bearer token from https://developer.twitter.com/, add it to your environment or hardcode in the script e.g. `export 'BEARER_TOKEN'='AAAAAAAAAAA...'` 
* Finally run the script! `python3 art-party.py`

## Example Output
![](output.png?raw=true)

## Caveat Emptor
The particular twitter API used in question only looks at the previous 7 days of tweets, so don't leave it too long after your party!


## Licence

MIT

