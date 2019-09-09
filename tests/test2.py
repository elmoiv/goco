import goco

GoogleApi = goco.Goco('client_secret.json', 'credentials.storage')

MyBlog = GoogleApi.connect(scope='Blogger', service_name='blogger', version='v3')

Posts = MyBlog.posts().list(blogId='7599400532066909387')

print(Posts.execute())

input()