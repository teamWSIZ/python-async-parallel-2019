import requests

class Photo:
    def __init__(self, albumId=0, id=0, title='', url='', thumbnailUrl=''):
        self.albumId = albumId
        self.id = id
        self.title = title
        self.url = url
        self.thumbnailUrl = thumbnailUrl

    # repr to coś w stylu __str__ , ale jest call-owane automatycznie przy drukowaniu listy
    def __repr__(self):
        return f'(albumId:{self.albumId}, id:{self.id}, title:{self.title}, url:{self.url})'


url = 'https://jsonplaceholder.typicode.com/photos'

response = requests.get(url)
photos = []
for p in response.json():
    photos.append(Photo(**p))
# print(response.json()[0])
# print(photos)
for p in photos:
    print(p)


# zadanie1 -- wypisać wszystkie Photo's które w tytule mają słowo 'nobis'
# zadanie2 -- z url'a: https://jsonplaceholder.typicode.com/todos wypisać todo's dla usera id = 2