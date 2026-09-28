#!/bin/bash
# Install Arduino IDE 2.3.10 + fix sandbox error in Ubuntu - run: bash fix-arduino.sh

sudo apt update
sudo apt upgrade -y

sudo apt install -y libfuse2

mkdir -p ~/Applications
wget -O ~/Applications/arduino-ide_2.3.10_Linux_64bit.AppImage \
	https://downloads.arduino.cc/arduino-ide/arduino-ide_2.3.10_Linux_64bit.AppImage
	
chmod +x ~/Applications/arduino-ide_2.3.10_Linux_64bit.AppImage

sudo tee /etc/apparmor.d/arduino-ide >/dev/null << 'EOF'
abi <abi/4.0>,
include <tunables/global>

profile arduino-ide /home/*/Applications/arduino-ide*.AppImage flags=(unconfined) {
	userns,
	include if exists <local/arduino-ide>
}
EOF

sudo apparmor_parser -r /etc/apparmor.d/arduino-ide

echo "Done. Run: ~/Applications/arduino-ide_2.3.10_Linux_64bit.AppImage"

