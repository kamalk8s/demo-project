from os import path
import os, subprocess


if not path.exists('src/db/data'):
    os.mkdir('src/db/data')

# update = input("Do you want to run apt update & upgrade? [y/n]: ")
update = 'y'

if update.lower() == 'y':
    # Updating the System
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])

# Installing Python
if (subprocess.run(['python3', '--version']).returncode != 0):
    print('Python3 not found.')
    installPython = subprocess.run(['sudo', 'apt', 'install', 'python3', '-y'])
    if installPython.returncode == 0:
        print('Python installation successful :)')
else:
    print('Requirement 1: Python found.')

# Installing PIP3
if (subprocess.run(['pip3', '--version']).returncode != 0):
    print('Pip3 not found.')
    installPython = subprocess.run(['sudo', 'apt', 'install', 'python3-pip', '-y'])
    if installPython.returncode == 0:
        print('Pip3 installation successful :)')
else:
    print('Requirement 2: Pip3 found.')

# Installing Docker
if (subprocess.run(['docker', '--version']).returncode != 0):
    print('Docker not found.')
    installPython = subprocess.run(['sudo', 'apt', 'install', 'docker.io', '-y'])
    subprocess.run(['sudo', 'systemctl', 'enable', 'docker'])
    subprocess.run(['sudo', 'systemctl', 'start', 'docker'])
    subprocess.run(['sudo', 'groupadd', 'docker'])
    subprocess.run(['sudo', 'usermod', '-aG', 'docker', '$USER'])
    subprocess.run(['newgrp', 'docker'])
    if installPython.returncode == 0:
        print('Docker installation successful :)')
else:
    print('Requirement 3: Docker found.')

# Installing Docker-Compose
if (subprocess.run(['docker-compose', '--version']).returncode != 0):
    print('Docker-Compose not found.')
    installPython = subprocess.run(['sudo', 'apt', 'install', 'python3-pip', '-y'])
    if installPython.returncode == 0:
        print('Docker-Compose installation successful :)')
else:
    print('Requirement 4: Docker-Compose found.')

# DONE
print('\nDone. To run containers: docker-compose up')
