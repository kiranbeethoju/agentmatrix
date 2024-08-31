from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentmatrix",
    version="0.2.0",
    author="Kiran Beethoju",
    author_email="kiranbeethoju@gmail.com",
    description="A multi-agent system for processing queries using DuckDuckGo and LLM agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiranbeethoju/agentmatrix",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "openai",
    ],
)