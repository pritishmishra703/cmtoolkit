from setuptools import setup, find_packages

setup(
    name="cmtoolkit",
    version="1.0.0",
    description="This package makes Confusion Matrix no more a confusion",
    author="Pritish Mishra",
    author_email="pritishmishra23@gmail.com",
    url="https://github.com/pritishmishra703/cmtoolkit",
    packages=find_packages(),
    install_requires=[
   'numpy',
   'matplotlib'
]
)
