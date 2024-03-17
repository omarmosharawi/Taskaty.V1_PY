from setuptools import setup

setup(
    name='Taskaty',
    version='0.1',
    description="Simple CLI Task Manger",
    author='Omar Mohamed Sharawi',
    install_requires=[
        'tabulate'
    ],
    entry_point={
        'console_scripts': [
            'app=app:main',
        ],
    }
)
