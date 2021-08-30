import subprocess

## Feed the data
subprocess.run(['sudo', 'chmod', '+x', './tools/data-feeder.sh'])
if (subprocess.run(['http', '--version']).returncode != 0):
    installPython = subprocess.run(['sudo', 'apt', 'install', 'httpie', '-y'])
    if installPython.returncode == 0:
        feeder = subprocess.run(['source', './tools/data-feeder.sh'])
    else:
        print('Data Feed Failed. Make sure you have installed httpie')
else:
    feeder = subprocess.run(['/bin/bash', './tools/data-feeder.sh'])
subprocess.run(['sudo', 'chmod', '-x', './tools/data-feeder.sh'])