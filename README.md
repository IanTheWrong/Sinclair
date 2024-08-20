# Sinclair
CLI Password Manager

# Installation
requirements: Python, pip, git, pyenv, venv Linux, Mac, or Windows (I don't use windows so I can't tell you if there are any differences)

create a virtual environment, activate it (linux it's ```source <name>/bin/activate```)

```git clone https://github.com/IanTheWrong/Sinclair```

```pip install setuptools```

```pip install -e /path/to/script/folder```

installation should now be done. simply call "sinclair" to start the program in terminal

[https://stackoverflow.com/questions/27494758/how-do-i-make-a-python-script-executable]
[https://setuptools.pypa.io/en/latest/userguide/quickstart.html]

# Setup
Uncomment all the commented lines, and comment all the uncommented lines, flip flop.
except for line 10. Keep that no matter what.

Fill in the Key and Password with whatever password you desire
Username is what is needed to reset your password. Like a safety sentence.

Run it once.

Return to the original format. I will eventually change this to another setup.

# Usage

**reset**
resets your password, will ask for your username in order to reset.

**set:**
adds a new login credential. Origin is what the username password is for, i.e Discord, Reddit, Github, e621

**get:**
gets one of your already saved credentials, based on the origin

**delete:**
deletes a credential, based on the origin
