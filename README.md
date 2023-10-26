# Digital photo frame scripts for Raspberry pi

## Install requirements as root

sudo -i

python3.7 -m pip install -r requirements.txt --user

#### If you don't have python3.7

sudo apt-get update -y

sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y

wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz

tar xf Python-3.7.4.tar.xz

cd Python-3.7.4

./configure

make -j 4

sudo make altinstall

sudo rm -r Python-3.7.4

rm Python-3.7.4.tar.xz

sudo apt-get --purge remove build-essential tk-dev -y

sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev -y

sudo apt-get --purge remove libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev -y

sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y

sudo apt-get autoremove -y

sudo apt-get clean


## Downscale images
e.g.: python3 convert --folder ~/Pictures


## Digital photo frame
Copy rc.local to /etc/rc.local

Copy startup.py and startup.sh to /home/pi/

chmod +x startup.sh

## Turn on display overscan 
echo 'disable_overscan=1' | sudo tee -a /boot/config.txt

## Disabling the blank screen
echo '[SeatDefaults]' | sudo tee -a /etc/lightdm/lightdm.conf && echo 'xserver-command=X -s 0 -dpms' | sudo tee -a /etc/lightdm/lightdm.conf

## Reboot Raspberry
sudo reboot

After reboot, startup.py should start automatically. If it is not visible in the running processes (htop) then check the /home/pi/python_log.txt file.


