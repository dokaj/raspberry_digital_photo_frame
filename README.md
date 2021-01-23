#Digital photo frame scripts for Raspberry pi

## Downscale images
python convert --folder ~/Pictures


## Digital photo frame
Copy rc.local to /etc/rc.local

Copy startup.py and startup.sh to /home/pi/


## Turn off low voltage warning
echo 'avoid_warnings=1' | sudo tee -a /boot/config.txt
echo 'disable_overscan=1' | sudo tee -a /boot/config.txt

## Disabling the blank screen
echo '[SeatDefaults]' | sudo tee -a /etc/lightdm/lightdm.conf && echo 'xserver-command=X -s 0 -dpms' | sudo tee -a /etc/lightdm/lightdm.conf
