sudo apt update
sudo apt-get -y install apache2
sudo apt install libjpeg-dev zlib1g-dev
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9
sudo apt-get install python3-pip python-dev
pip3 install torch==1.8+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
python3 server_base.py
