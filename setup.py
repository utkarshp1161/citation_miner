from setuptools import setup, find_packages

setup(
    name='citation_miner',
    version='1.0.0',  # Update with your module's version
    description='citation miner',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Utkarsh Pratiush',
    author_email='utkarshp1161@gmail.com',
    url='https://github.com/utkarshp1161/citation_miner',  # Replace with your module's GitHub repository URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)