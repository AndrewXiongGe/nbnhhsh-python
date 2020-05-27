import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbnhhsh-python",
    version="0.0.1",
    author="purofle",
    author_email="3272912942@qq.com",
    description="nbnhhsh的python版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/purofle/nbnhhsh-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
