import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convert-full-url-pkg-sshmuylovich", # Replace with your own username
    version="0.0.1",
    author="Sima Shmuylovich",
    author_email="sshmuylovich21@andover.edu",
    description="This package converts partial urls into full urls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sshmuylovich/Convert_Full_URL.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)