from setuptools import setup, find_packages

setup(
    name="fastapi-hosting-master",
    version="0.1.0",
    packages=find_packages(include=["app", "app.*"]),
    package_dir={'': '.'}, 
    install_requires=[
        "fastapi==0.88.0",
        "uvicorn==0.20.0",
        "anyio==3.6.2",
        "click==8.1.3",
        "colorama==0.4.6",
        "h11==0.14.0",
        "idna==3.4",
        "pydantic==1.10.2",
        "sniffio==1.3.0",
        "starlette==0.22.0",
        "typing_extensions==4.4.0"
    ],
    entry_points={
        "console_scripts": [
            "start-fastapi = app.cli:main"
        ]
    },
    author="Abhishek Rajput",
    author_email="abhishek25022004@gmail.com",
    description="A simple FastAPI application",
    url="https://github.com/Abhishek-2502/FastAPI_Deploy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
