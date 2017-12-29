from setuptools import setup, find_packages

setup(
    name='flask_json_content_type_validator',
    packages=find_packages(),
    version='0.1.0',
    description='Flask JSON Content-Type decorator which validates that the '
    'Content-Type is indeed application/json. In the case of a wrong content '
    'type, then the decorator will throw an exception which can be customized.',
    long_description=open('README.md').read(),
    author='Victor Klapholz',
    author_email='victor.klapholz@gmail.com',
    url='https://github.com/vklap/flask-json-content-type-validator',
    keywords='flask json content validation decorator',
    license='MIT',
    install_requires=[
        "Flask==0.12.2"
    ],
    tests_require=[]
)
