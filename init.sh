sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test

# sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
# sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application

sudo /etc/init.d/gunicorn restart
