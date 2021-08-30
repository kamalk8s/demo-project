Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  # config.vm.network "forwarded_port", guest: 81, host: 80
  # config.vm.network "forwarded_port", guest: 8080, host: 8080
  # config.vm.network "forwarded_port", guest: 8081, host: 8081
  config.vm.network "private_network", ip: "192.168.10.10"
  config.vm.synced_folder ".", "/demo-project"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
  end
  
  config.vm.provision "shell", inline: <<-SHELL
    apt update && apt -y upgrade
    apt install -y git
    apt install -y python3.9
    apt install -y python3-pip
    apt install -y docker.io
    systemctl enable docker
    systemctl start docker
    usermod -aG docker $USER
    newgrp docker
    sudo apt -y install docker-compose
    cd /
    # git clone https://github.com/kamalk8s/demo-project.git
    cd demo-project
    python3 ./tools/install-requirements.py
    docker-compose up --build -d
    echo "Open URL: http://192.168.10.10"
  SHELL
end
