# FastAPI_Deployment
Complete Guide to deploy FastAPI. Below are the steps to deploy FastAPI on AWS EC2 and access it through anywhere on the internet.

### Built With

- [Fastapi](https://github.com/tiangolo/fastapi)
- [Python](https://www.python.org/)
- [AWS](https://aws.amazon.com/)

## Getting Started

### Prerequisites

We assume that you have a Amazon EC2 instance (Amazon Linux).

### Installation

After you enter the instance by ssh or any other method, update the instance first by using below command:

```sh
sudo yum update -y
```

Command to install python :

```sh
sudo yum install -y python3
```


Command to install git to clone the repository :

```sh
sudo yum install -y git
```

Command to check python version:

```sh
sudo python3 --version
```

Command to check git version :

```sh
sudo git --version
```

Command to clone the repository.

```sh
sudo git clone https://github.com/Abhishek-2502/FastAPI_Deploy
```

Command to change location into the cloned folder. You can use your own repository name :

```sh
cd FastAPI_Deploy
```

IN CASE OF SETUP.PY FILE:

Command to install all the requirements required for the project.

```sh
sudo python3 setup.py install
```  

Command to check our package is installed or not (Following command should return a path):

```sh
which start-fastapi
```

Command to run the package:

```sh
start-fastapi
```

IN CASE OF REQUIREMENTS.TXT FILE:

Command to install all the requirements required for the project.

```sh
sudo python3 -m pip install -r requirements.txt
``` 

Command to run the api.

```sh
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

After running go to AWS instance --> Security tab --> Edit inbound rules --> Create rule --> Select All traffic and IPv4<br>

Go to the public ip provided by the instance add :8000 in the end as our api is running at that particular port.


Other Commands:

To delete directory in ubuntu:
```sh
sudo rm -rf Directory_Name
```

