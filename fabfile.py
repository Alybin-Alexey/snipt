from fabric.api import cd, local, env, run, sudo

import datetime


env.hosts = ['nick@snipt.net:39039']
env.site_path = '/var/www/snipt'
env.venv_path = '/home/nick/.virtualenvs/snipt'

def _python(cmd):
    return env.venv_path.rstrip('/') + '/bin/python ' + cmd

def deploy():
    local('python manage.py collectstatic --ignore grappelli --ignore admin --noinput')

    try:
        local('hg push')
    except:
        pass

    with cd(env.site_path):
        run('hg pull -u')
        run(_python('manage.py collectstatic --ignore grappelli --ignore admin --noinput'))

def re():
    with cd(env.site_path):
        run('./gk')
        run('/home/nick/.virtualenvs/snipt/bin/python /home/nick/.virtualenvs/snipt/bin/gunicorn -c gunicorn.conf.py debug_wsgi:application')

def db_backup():

    filename = datetime.datetime.now().strftime('%m-%d-%y')

    print filename

    #run('pg_dump snipt > snipt.pgdump')

    #conn = S3Connection('AKIAJJRRQPTSPKB7GYOA', 'DIYz2g5vPjcWE4/YI7wEuUVAskwJxs2llFvGyI1a')
    #snipt_bucket = conn.get_bucket('snipt')

    #k = Key(snipt_bucket)
    #k.set_contents_from_filename('snipt.pgdump')
