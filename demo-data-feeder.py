import subprocess

## Feed the data
subprocess.run(['sudo', 'chmod', '+x', './demo-api/data-feeder/data-feeder.sh'])
if (subprocess.run(['http', '--version']).returncode != 0):
    installPython = subprocess.run(['sudo', 'apt', 'install', 'httpie', '-y'])
    if installPython.returncode == 0:
        feeder = subprocess.run(['source', './demo-api/data-feeder/data-feeder.sh'])
    else:
        print('Data Feed Failed. Make sure you have installed httpie')
else:
    feeder = subprocess.run(['/bin/bash', './demo-api/data-feeder/data-feeder.sh'])
subprocess.run(['sudo', 'chmod', '-x', './demo-api/data-feeder/data-feeder.sh'])