from setuptools import setup

setup(
    name='Demo Application',
    version='1.0',
    long_description=__doc__,
    packages=['demo'],
    scripts=['bin/demo-hello'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.1',
        'gunicorn==19.9.0'
    ]
)
