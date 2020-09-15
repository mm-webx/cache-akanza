# Loadtest
https://www.npmjs.com/package/loadtest
   
    sudo npm install -g loadtest
    loadtest -c 10 --rps 200 http://mysite.com/

# Data
Create test data
    
    from post.models import *
    from django.contrib.auth.models import User
    for i in range(10):
        u = User.objects.create(first_name=f"First {i}", last_name=f"Last {i}",
                                email=f'{i}@wp.pl',
                                username=f"user{i}",
                                is_active=True)
        for j in range(50):
            p = Post.objects.create(title=f'Post title #{j}',
                                    content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                                    author=u)
            for k in range(5):
                g = Gallery.objects.create(title=f'Gallery title #{j}-{k}', post=p)
                fs = []
                for l in range(10):
                    fs.append(Photo(gallery=g,
                                    description=f"Nice image #{l}",
                                    photo_url="https://images.unsplash.com/photo-1505015390928-f9e55218544f?ixlib=rb-1.2.1&auto=format&fit=crop&w=150&q=80"))
                Photo.objects.bulk_create(fs)
                print(f'{i}/10 {j}/50 {k}/5')
                    
                    # cache-akanza
# cache-akanza
