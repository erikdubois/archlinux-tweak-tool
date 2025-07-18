#!/bin/bash
#set -e
##################################################################################################################
# Author    : Erik Dubois
# Website   : https://www.erikdubois.be
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################
#tput setaf 0 = black
#tput setaf 1 = red
#tput setaf 2 = green
#tput setaf 3 = yellow
#tput setaf 4 = dark blue
#tput setaf 5 = purple
#tput setaf 6 = cyan
#tput setaf 7 = gray
#tput setaf 8 = light blue
##################################################################################################################

workdir=$(pwd)

./chaotic

# reset - commit your changes or stash them before you merge
# git reset --hard - personal alias - grh

if [[ -f "./repo.sh" ]]; then
    echo "Found repo.sh, running it..."
    bash ./repo.sh
fi

echo "getting latest .bashrc"
wget https://raw.githubusercontent.com/erikdubois/edu-shells/refs/heads/main/etc/skel/.bashrc-latest -O $workdir/usr/share/archlinux-tweak-tool/data/arco/.bashrc

echo "getting latest .zshrc"
wget https://raw.githubusercontent.com/erikdubois/edu-shells/refs/heads/main/etc/skel/.zshrc -O $workdir/usr/share/archlinux-tweak-tool/data/arco/.zshrc

echo "getting latest config.fish"
wget https://raw.githubusercontent.com/erikdubois/edu-shells/refs/heads/main/etc/skel/.config/fish/config.fish -O $workdir/usr/share/archlinux-tweak-tool/data/arco/config.fish
wget https://raw.githubusercontent.com/erikdubois/edu-shells/refs/heads/main/etc/skel/.config/fish/config.fish -O $workdir/usr/share/archlinux-tweak-tool/data/arch/config.fish

########### Arch Linux
echo "getting archlinux keyring"
rm $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/keyring/*
#rm $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/mirrorlist/*
#get latest archlinux-keyring
wget https://archlinux.org/packages/core/any/archlinux-keyring/download --content-disposition -P $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/keyring/
#wget https://archlinux.org/packages/core/any/archlinux-mirrorlist/download --content-disposition -P $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/mirrorlist/

# Below command will backup everything inside the project folder
git add --all .

git commit -m "update"

# Push the local files to github

if grep -q main .git/config; then
	echo "Using main"
		git push -u origin main
fi

if grep -q master .git/config; then
	echo "Using master"
		git push -u origin master
fi

echo "################################################################"
echo "###################    Git Push Done      ######################"
echo "################################################################"
