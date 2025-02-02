# Fastapi-hosting
Complete Guide for hosting fastapi. Below are the steps for hosting fastapi on aws ec2 and access it through anywhere on the internet.

### Built With

- [Fastapi](https://github.com/tiangolo/fastapi)
- [Python](https://www.python.org/)
- [AWS](https://aws.amazon.com/)

## Getting Started

### Prerequisites

We assume that you have a amazon ec2 instance.
After you enter the instance by ssh or any other method update the instance first by using below command:

```sh
sudo apt-get update
```

Command to install python :

```sh
sudo apt install python3-pip
```


Command to install git to clone this repository :

```sh
sudo apt install git
```

Command to install git to clone this repository. You can use your own repository git url which you want to host :

```sh
sudo git clone https://github.com/Abhishek-2502/FastAPI_Deploy
```

Command to change location into the cloned folder. You can use your own repository name :

```sh
cd FastAPI_Deploy
```

Command to install all the requirements required for the project to run. In our case we have created setup.py file, you can also create your own requirements :

```sh
pip install .
```  

if not works then

```sh
pip install . --break-system-packages
```  


Command to install all the requirements required for the project to run using requirements.txt file.
pip install -r requirements.txt
```

Command to run the API when using setup.py file:

```sh
python3 -m start-fastapi
```

Command to run the API when using requirement.txt file:

```sh
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

After running go to AWS instance --> Security tab --> Edit inbound rules --> create rule --> Enable access from anywhere.<br>
Go to the public ip provided by the instance add :8000 in the end as our api is running at that particular port.

That's it you can now access your Fastapi from anywhere.


Other Commands:

To create Virtual Environment:

```sh
python3 -m venv venv
```
```sh
source venv/bin/activate
```

To delete directory:
```sh
sudo rm -rf Directory_Name
```

To run python commands:
```sh
python3 -m command_of_python
```

