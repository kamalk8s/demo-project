## HOW TO CONFIGURE

- Clone this repository `git clone https://github.com/kamalk8s/demo-project.git`

### For Windows

- Install Vagrant from [here](https://www.vagrantup.com/downloads).
- Go to CMD/PowerShell and
- Run `vagrant up` inside demo-project folder.

### For Linux

- Install Vagrant using `sudo apt install vagrant` or visit [vagrant download page](https://www.vagrantup.com/downloads).
- Run `vagrant up` inside demo-project folder.

## CONFIRM THE INSTALLATION

- Go to [http://192.168.10.10](http://192.168.10.10) on your host machine. If works, frontend is working fine.
- Install httpie [`sudo apt install httpie`] or use postman to send get request to 192.168.10.10:8080. Example: `http http://192.168.10.10:8080`. If return-code is 200, db is running fine.
- Similarly `http http://192.168.10.10:8081` return return-code of 200, means API server is also working as expected.

Alternatively, if you're able to submit data on 192.168.10.10, application is working fine.

## WHERE TO USE

- To learn DevOps, you can use this project as 3 containers driven services.
- To learn basics about Python - Flask framework.
- To create a docker ready infrastructure on your Windows/Linux device.
