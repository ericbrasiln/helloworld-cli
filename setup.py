from setuptools import setup
setup(
    name = 'resumos-anpuh-cli',
    version = '0.1.0',
    packages = ['resumosanpuh'],
    install_requires = ['requirements.txt'],
    entry_points = {
        'console_scripts': [
            'resumosanpuh = resumosanpuh.__main__:main'
        ]
    })