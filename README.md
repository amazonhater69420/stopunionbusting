# stopunionbusting
Whichever Amazon employee created doitwithoutdues.com is a scab

you'll need Selenium WebDriver, Firefox, and GeckoDriver to run this (i know this is not an elegant solution, but i'm not smart enough to write a better one.)

on Linux:

Ubuntu
    sudo apt install python-pip
    sudo pip install selenium
    wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-linux64.tar.gz
    tar -xzf geckodriver\*.tar.gz
    chmod +x geckodriver
    sudo mv geckodriver /usr/local/bin

Arch
    sudo pacman -S python-selenium geckodriver
    <your AUR installation command here> selenium-server-standalone

NOTE:
if you run this a bunch it seems like their DDOS or whatever protection will block you

i got the names from here:
https://github.com/dominictarr/random-name