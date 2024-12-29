# forum

## install

```
git clone https://github.com/niux3/forum.git
cd forum
mkdir .venv
pipenv shell
pipenv install
./manage.py migrate
./manage.py create_themes
```

if you want populate database

```
./manage.py create_users
./manage.py create_boards
./manage.py create_topics
./manage.py create_posts
```

How to launch application ?

```
./manage.py runserver
```

## screenshots

![home](./apps/core/static/img/screenshots/capturepage-1.png)
![search](./apps/core/static/img/screenshots/capturepage-2.png)
![mp](./apps/core/static/img/screenshots/capturepage-3.png)
![my topics](./apps/core/static/img/screenshots/capturepage-4.png)
![get password](./apps/core/static/img/screenshots/capturepage-5.png)
![signin](./apps/core/static/img/screenshots/capturepage-6.png)
![new post](./apps/core/static/img/screenshots/capturepage-7.png)
![see profil](./apps/core/static/img/screenshots/capturepage-8.png)
![all topics](./apps/core/static/img/screenshots/capturepage-9.png)
![post](./apps/core/static/img/screenshots/capturepage-10.png)
