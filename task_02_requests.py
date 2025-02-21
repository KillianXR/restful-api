#!/usr/bin/env python3
import requests
import csv

"""
module that treat a API data
"""


def fetch_and_print_posts():
    """function that fetch API posts and prints the title"""

    answer = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'status code: {answer.status_code}')

    if answer.status_code == 200:
        posts = answer.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """function that fetch API posts and save it into a csv file"""

    answer = requests.get('https://jsonplaceholder.typicode.com/posts')
    if answer.status_code == 200:
        posts = answer.json()
        for post in posts:
            data = {'id': post['id'], 'title': post['title'], 'body': post['body']}

        with open('post.csv', 'w', newline='') as csvfile:
            data = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, data=data)
            writer.writeheader()
            writer.writerows(data)
