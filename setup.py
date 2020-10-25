import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord-webhook",
    version="0.0.1",
    author="JtheDroid",
    author_email="fabi.jobo@gmail.com",
    description="A package with classes for Discord webhooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JtheDroid/discord-webhook",
    packages=setuptools.find_packages(),
    python_requires='>=3',
)
