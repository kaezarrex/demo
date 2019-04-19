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
        'Flask==0.12.3',
        'gunicorn==19.5.0'
    ]
)
