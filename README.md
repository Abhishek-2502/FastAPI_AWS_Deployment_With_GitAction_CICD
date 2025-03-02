# FastAPI_AWS_Deployment_With_GitAction_CICD
Complete Guide to Deploy FastAPI app on AWS and develop CICD Pipeline on AWS EC2.

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

Command to install python and pip :

```sh
sudo yum install python3-pip -y
```

Command to upgrade pip:

```sh
pip3 install --upgrade pip
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

Command to check pip version :

```sh
pip3 --version
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

Access the website from "Public IPv4 address" provided by the instance and add :8000 in the end as our api is running at that particular port.


### CICD Integration (For Setup.py)

1. Under Git Action, select set up a workflow yourself.

2. Add following code in main.yml and make name changes according to your repo

```sh
name: Deploy to EC2

on:
  push:
    branches:
      - main  # Trigger on push to the main branch

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    # Checkout the code from the repository
    - name: Checkout code
      uses: actions/checkout@v3

    # Set up SSH agent to use the private key stored in GitHub Secrets
    - name: Set up SSH
      uses: webfactory/ssh-agent@v0.5.3
      with:
        ssh-private-key: ${{ secrets.EC2_SSH_PRIVATE_KEY }}

    # Deploy to EC2
    - name: Deploy to EC2
      run: |
        ssh -o StrictHostKeyChecking=no ec2-user@${{ secrets.EC2_HOST }} << 'EOF'
          cd /home/ec2-user/FastAPI_Deploy
          sudo chown -R ec2-user:ec2-user .  # Change ownership of the whole repo
          sudo chmod -R u+rw .  # Ensure read/write permissions for the user
          git config --global --add safe.directory /home/ec2-user/FastAPI_Deploy  # Add the repo to safe directory
          git pull origin main  # Pull latest code

          # Add any additional deployment commands here
          # Install dependencies via setup.py
          sudo python3 setup.py install

          # Stop existing FastAPI process safely
          PID=$(pgrep -f "uvicorn")
          if [ ! -z "$PID" ]; then
            echo "Stopping existing FastAPI process with PID $PID"
            kill -9 $PID
          fi
    
          # Start FastAPI in the background
          nohup start-fastapi > fastapi.log 2>&1 &
    
          echo "FastAPI restarted successfully!"
        EOF
```

3. In EC2 instance, type following commands to get Secret Keys.

Command to generate secret key:

```sh
sudo ssh-keygen -t rsa -b 4096 -f ~/.ssh/github-deploy

```

Command to give permissions:
```sh
sudo chmod 600 ~/.ssh/authorized_keys
```

Command to see public key:

```sh
sudo cat ~/.ssh/github-deploy.pub
```

Command to set public key:

```sh
sudo cat ~/.ssh/github-deploy.pub >> ~/.ssh/authorized_keys
```

Command to get private key:
```sh
sudo cat ~/.ssh/github-deploy
```

4. Get your Public IPv4 DNS from EC2 Instance from right side.<br> Ex: ec2-64-0-123-xxx.ap-south-1.compute.amazonaws.com

5. Goto Settings of repo and than Security-> Secrets and Variables-> Actions, add following Variables:<br>
    EC2_HOST : Pubic_IPv4_DNS from Step 4<br>
    EC2_SSH_PRIVATE_KEY : Private key from Step 3

6. Pull all the updated code than push some code for testing.

7. Goto Git Action for seeing the workflow lifecycle.

8. Access the website from "Public IPv4 address" provided by the instance and add :8000 in the end as our api is running at that particular port.




Other Commands:

To see hidden directory and files:
```sh
dir -a
```

To delete directory in ubuntu:
```sh
sudo rm -rf Directory_Name
```

