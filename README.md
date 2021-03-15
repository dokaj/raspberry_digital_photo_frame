# Digital photo frame scripts for Raspberry pi

## Install requirements as root

su root

pip3 install -r requirements.txt

## Downscale images
e.g.: python3 convert --folder ~/Pictures


## Digital photo frame
Copy rc.local to /etc/rc.local

Copy startup.py and startup.sh to /home/pi/


## Turn on display overscan 
echo 'disable_overscan=1' | sudo tee -a /boot/config.txt

## Disabling the blank screen
echo '[SeatDefaults]' | sudo tee -a /etc/lightdm/lightdm.conf && echo 'xserver-command=X -s 0 -dpms' | sudo tee -a /etc/lightdm/lightdm.conf


