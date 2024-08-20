from setuptools import setup
setup(
    name='sinclair',
    version='1.0.0',
    entry_points={
        'console_scripts' : [
            'sinclair=sinclair:main'
        ]
    }
)