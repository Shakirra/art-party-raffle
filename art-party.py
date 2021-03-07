import requests
import os
import json
import random

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

tagname = 'HungerArtParty'

def hostList():
    return ['ArishiShakirr']

def auth():
    return os.environ.get("BEARER_TOKEN")
    


def create_url(next_token):
    query = "%23{} -is:retweet has:media".format(tagname)
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id"
    expansions = "expansions=author_id"

    #print(query)
    if next_token == "none":
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}&max_results=100".format(
            query, tweet_fields, expansions
        )
    else: 
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}&max_results=100&next_token={}".format(
            query, tweet_fields, expansions, next_token
        )
    #print(url)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    print("Searching tweets tagged #{}...".format(tagname))

    bearer_token = auth()
    url = create_url("")
    headers = create_headers(bearer_token)
    
    totalTweets = 0
    users = []
    next_token = "none"
    
    while next_token: 
        url = create_url(next_token)
        json_response = connect_to_endpoint(url, headers)
        #print(json.dumps(json_response, indent=4, sort_keys=True))
        totalTweets = totalTweets + json_response['meta']['result_count']
        if totalTweets > 0:
            users = users + json_response['includes']['users']
        next_token = json_response['meta'].get('next_token')


    print("{} tagged tweets found.".format(totalTweets))

    filteredUsers = list(filter(lambda item: item['username'] not in hostList(), users))
    distinctUsers = list(set(map(lambda item: "{} | @{}".format(item['name'], item['username']), filteredUsers)))
    print("Total {} users, excluding {} found.".format(len(distinctUsers), hostList()))
    
    print('SPIN THE WHEEL! 彡ﾟ◉ω◉ )つー☆* ')
    random.shuffle(distinctUsers)
    for x in range(0, min(10, len(distinctUsers))):
        print("{}. {}".format(x+1, distinctUsers[x]))
    



if __name__ == "__main__":
    main()
