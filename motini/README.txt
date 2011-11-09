Start it up with:
uwsgi --reaper --vacuum --master --processes 1 --single-interpreter --plugins python --enable-threads --protocol=http --socket=0.0.0.0:6534 wsgi.py
