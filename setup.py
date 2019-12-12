import os, sys
from shutil import which

# write token value to ~/.ssh/DigitalOceanToken
if not os.path.exists(os.path.expanduser("~") + "/.ssh/DigitalOceanToken"):

    if len(sys.argv) == 1:
        ocean_token = input("Paste your Digital Ocean API token: ")
    elif len(sys.argv) == 2:
        ocean_token = sys.argv[1]
    else:
        raise ValueError

    dot = open(os.path.expanduser("~") + "/.ssh/DigitalOceanToken", "w")
    dot.write(ocean_token)
#7d125e626cdc8a86eb5cfcee68676c2a830dbdc681353ac457b759a82755d26c

py3_reqs = ["digitalocean", "tabulate"]
bash_reqs = ["brew", "python3"]

# install homebrew and python3 if not installed
for bash in bash_reqs:
    if which(bash) is None:
        if bash == "brew":
            os.system("/usr/bin/ruby -e \"$(curl -fsSL "
                      "https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
        elif bash == "python3":
            os.system("brew install python3")


# install each pip package necessary
try:
    (__import__(pip) for pip in py3_reqs)
except ImportError:
    print("Required packages not available. Installing...")
    os.system("pip3 install -r src/requirements.txt")


print("Copying \'ocean\' to ~/.bin/ ...")
os.system("cp -rf src/ocean ~/.bin")






