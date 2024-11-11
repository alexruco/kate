from setuptools import setup, find_packages

setup(
    name="kate",
    version="0.1.2",
    description="An interface to interact with various AI models, including OpenAI and LLaMA 3 via Ollama.",
    author="Alex Ruco",
    author_email="alex@ruco.pt",
    url="https://github.com/alexruco/kate",
    packages=find_packages(),
    install_requires=[
        "openai>=0.01.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
