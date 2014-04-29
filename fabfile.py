from fabric.api import *

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '/tmp/demo.tar.gz')
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    run('mkdir /tmp/demo')
    with cd('/tmp/demo'):
        run('tar xzf /tmp/demo.tar.gz')
        with cd('/tmp/demo/%s' % dist):
            # now setup the package with our virtual environment's
            # python interpreter
            run('/var/www/demo/env/bin/python setup.py install')
            run('cp -r demo/static /var/www/demo/')
    # now that all is set up, delete the folder again
    run('rm -rf /tmp/demo /tmp/demo.tar.gz')

    # update configs
    put('gunicorn.conf', '/var/www/demo/gunicorn.conf')

    put('upstart/demo.conf', '/etc/init/demo.conf', use_sudo=True)
    sudo('ln -sf /lib/init/upstart-job /etc/init.d/demo')

    # reload services
    sudo('service demo reload')

def bootstrap():
    sudo('mkdir /var/www/demo')
    sudo('chown %s:%s /var/www/demo' % (env.user, env.user))
    with cd('/var/www/demo'):
        run('virtualenv --distribute env')

    sudo('touch /var/log/demo-access.log')
    sudo('chown nobody:nogroup /var/log/demo-access.log')
