# ILO fans hack
Simple python script for HP ProLiant server`s fans autoconfiguration.
<div><strong>For ILO versions < 2.73 only!</strong></div>
Has been tested with HP DL 380 gen 9 and ILO 2.73.
<a href="https://www.youtube.com/watch?v=Keyz-9HNr7Q">A useful guide (recommended to watch)</a>

## How to use (Linux guide)

### - Install <i>python3, pip3, venv, git</i>
For example: 
<code>apt install python3 python3-pip python3-venv git</code>
<code>pacman -S python3 python3-pip3 python3-venv git</code>

### - Clone this repository
```bash
git clone https://github.com/SamanuelAdmin/ilo_fans_hack
cd ilo_fans_hack
```

### - Create your environment and activate it
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### - Install dependencies
```bash
pip3 install -r requirements.txt
```

### - Configure the script for your build
1) Create your own <code>.env</code> file using template file (<code>.env.template</code>)
2) Change config file (<code>config.conf</code>) for your needs.

### - Start script and wait for the end 
```bash
python3 main.py
```
