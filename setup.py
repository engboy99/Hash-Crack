from setuptools import setup, find_packages

setup(
    name="hash_crack",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "tensorflow",
        "numpy",
        "asyncio"
    ],
    entry_points={
        "console_scripts": [
            "hash_crack=hash_crack.main:main"
        ]
    },
    author="Your Name",
    description="An advanced hash cracking tool with AI integration.",
    license="MIT",
)
