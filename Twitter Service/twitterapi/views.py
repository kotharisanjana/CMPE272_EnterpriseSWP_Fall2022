from django.shortcuts import render,redirect
from requests_oauthlib import OAuth1Session
from django.http import JsonResponse
import os
import json
import configparser


# Create your views here.

## Author: Sanjana Rajesh Kotari and Naga Bathula
## This file contains the views for the Twitter API application.



def create_oAuth_session():
    config = configparser.ConfigParser()
    config.read('twitterapi/config.ini')
    
    consumer_key = config['TWITTER']['CONSUMER_KEY']
    consumer_secret = config['TWITTER']['CONSUMER_SECRET']
    access_token = config['TWITTER']['ACCESS_TOKEN']
    access_token_secret = config['TWITTER']['ACCESS_TOKEN_SECRET']
    
    oAuth_session = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)
    return oAuth_session


def create_tweet(request):    
    content = ''
    if request.method == 'POST':
        content = request.POST.get('content', '')
        
    print('Content:' + content);
    oAuth_session = create_oAuth_session()
    url = 'https://api.twitter.com/2/tweets'
    #params = {'status': content}
    
    payload = {"text": content}

    # Making the request
    response = oAuth_session.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
        headers={"Content-Type": "application/json"})
    
   # response = oAuth_session.post(url, params=params)
    print(response)
    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )
    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    
    return JsonResponse(json_response,json_dumps_params={'indent': 4})
    

def get_timeline_tweets(request):
    
    userid = ''
    user_handle=''
    if request.method == 'POST':
        user_handle = request.POST.get('content', '')

    userid_url = 'https://api.twitter.com/2/users/by/username/{}'.format(user_handle)
    oAuth_session = create_oAuth_session()    
    userid_response = oAuth_session.get(userid_url)
    if userid_response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(userid_response.status_code, userid_response.text)
        )
    userid = userid_response.json()['data']['id']
   
    user_timeline_url = 'https://api.twitter.com/2/users/{}/tweets'.format(userid)   
    response = oAuth_session.get(user_timeline_url)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )
    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json_response)

    return JsonResponse(json_response,json_dumps_params={'indent': 4})


  
def delete_tweet(request):
    content = ''
    if request.method == 'POST':
        content = request.POST.get('content', '')
        
    print('Content:' + content);
    oAuth_session = create_oAuth_session()
    
    response = oAuth_session.delete("https://api.twitter.com/2/tweets/{}".format(content))

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json_response)

    return JsonResponse(json_response,json_dumps_params={'indent': 4})
