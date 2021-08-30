Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.network "forwarded_port", guest: 81, host: 81
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 8081, host: 8081
  config.vm.network "private_network", ip: "192.168.10.10"
  # config.vm.synced_folder ".", "/app"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
  end
  
  config.vm.provision "shell", inline: <<-SHELL
    apt update && apt -y upgrade
    apt install -y git
    apt install -y python3.9
    cd /
    git clone https://github.com/kamalk8s/demo-project.git
    cd demo-project
    python3 ./tools/install-requirements.py
  SHELL
end
