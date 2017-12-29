from setuptools import setup

setup(
    name='flask_json_content_type_validator',
    packages=['flask_json_content_type_validator'],
    version='0.0.1',
    description='Flask JSON Content-Type decorator which validates that the '
    'Content-Type is indeed application/json. In the case of a wrong content '
    'type, then the decorator will throw an exception which can be customized.',
    author='Victor Klapholz',
    author_email='victor.klapholz@gmail.com',
    url='https://github.com/vklap/flask-json-content-type-validator',
    keywords='flask json content validation decorator',
    install_requires=[
        "Flask==0.12.2"
    ],
    tests_require=[]
)
