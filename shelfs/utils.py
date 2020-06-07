import requests
import json
#from django.conf import settings
#from imgurpython import ImgurClient
import logging
from django.contrib.auth.models import User

from .models import Book

PROXY_POOL = [
    'https://douban.uieee.com',
    'https://douban-api.uieee.com',
    'https://douban-api.now.sh',
    'https://douban-api.zce.now.sh',
    'https://douban-api-git-master.zce.now.sh'
]

HEADERS = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'}
ENDPOINT = '/v2/book/isbn/'

def get_by_isbn(user, isbn):

    try:
        book = Book.objects.get(isbn13 = isbn)
    except Book.DoesNotExist:
        bookDict = request_api(isbn)
        if bookDict == None:
            return None
        book = Book()
        book.bind(bookDict)

        # if 'images' in bookDict:
        #     if 'small' in bookDict['images']:
        #         book.image_url = upload_image(bookDict['images']['small'])
        #     else:
        #         return None
        # else:
        #     return None 
        
        book.save()
    user = User.objects.get(id = user.id)
    book.owners.add(user)

    return book


def request_api(isbn):
    for i in range(len(PROXY_POOL)):
        url = "{}{}{}".format(PROXY_POOL[i], ENDPOINT, isbn)
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            continue
        try:
            bookDict = json.loads(r.text)
            return bookDict if "title" in bookDict else None
        except Exception as e:
            logging.warning(e)
            continue
    return None

# def upload_image(url):
#     try:
#         client = ImgurClient(settings.CLIENT_ID, settings.CLIENT_SECRET)
#         result = client.upload_from_url(url, config=None, anon=True)
#     except Exception as e:
#         logging.warning(e)
#         return ""
    
#     if 'link' in result:
#         uploaded_url = result['link']
#     else:
#         return ""
    
#     return uploaded_url