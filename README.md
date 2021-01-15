# stopunionbusting

Whichever Amazon employee created https://doitwithoutdues.com is a scab.

This script will automatically generate and submit information to the doitwithoutdues.com contact form. By running this script, their site will become overwhelmed with submissions, thus supressing efforts to de-unionize Amazon.

The script is powered by Selenium WebDriver and GeckoDriver.

## Installation

1. Download the repository.

2. Run the following commands to install project dependencies.

Linux (Ubuntu):
```
sudo apt install python-pip
sudo pip install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz
tar -xzf geckodriver*.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin
```

Linux (Arch)
```
sudo pacman -S python-selenium geckodriver
<your AUR installation command here> selenium-server-standalone
```

## Usage

Run the script:

```
python ./main.py
```

## Additional Notes

If you run this script a bunch, it seems like their DDOS or whatever protection will block you.

Sources:

* Names: https://github.com/dominictarr/random-name
* Domains: https://github.com/ivolo/disposable-email-domains
