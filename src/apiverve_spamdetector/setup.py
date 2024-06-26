from setuptools import setup, find_packages

setup(
    name='apiverve_spamdetector',
    version='1.0.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Spam Detector is a simple tool for detecting spam in a text. It returns the spam score and the spam label.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
