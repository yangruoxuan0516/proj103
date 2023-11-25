# PROJ103
In this course, we are given
- a Raspberry Pi
- two wheels et two motors
- a motor controller
- a webcam
- some batteries
- some wooden boards
- other tools

we want to
- make a car who can run
- control the car via a web page
- enable the car to auto-control
- realise a collaboration between the cars

we can consult
- the forum: https://proj103.telecom-paris.fr
- the Gitlab: https://gitlab.telecom-paris.fr

## TURN OFF THE RASPBERRY PI BEFORE UNPLUGGING THE POWER
ENTER IN THE TERMINAL
> sudo shutdown

WAIT UNTIL IT IS TURNED OFF


## Installation of OS on SD card
Using Raspberry Pi Imager to install Raspberry Pi OS to a microSD card
### Settings
- OS: Lite 64
- user name: g7a
- password: g7a


## Connection to Wifi
Adding the "wpa_supplicant.conf" document to the SD card to realise Wifi connection on Raspberry Pi
### personal hotspot
"wpa_supplicant.conf" content
>country=FR  
ctrl_interface=DIR=/var/run/wps_supplicant GROUP=netdev  
update_config=1  
network={  
        ssid=‘<wifi_name>’  
        psk=‘<wifi_password>’  
}  

### campus wifi
"wpa_supplicant.conf" content
>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev  
update_config=1  
country=FR  
network={  
    ssid="Campus-Telecom"  
    scan_ssid=1  
    key_mgmt=WPA-EAP  
    ca_cert="/boot/tp-2021.pem"  
    eap=TTLS  
    identity="robotpi-34.enst.fr"  
    password="uPk69cfdwPs5qw"  
    phase2="auth=PAP"  
}  

ficher de certificat  
https://doc.telecom-paris.fr/reseau/param.html#parametres-de-configuration


## Connection to Raspberry Pi via ssh
### verification of Wifi connection
- personal hotspot  
  > ping g7a.local  

  - 或者查找树莓派ip，如果系统设置-网络-详细信息-IP地址为 172.20.10.2 则终端输入
    > nmap -sn 172.20.10.0/24

- campus wifi  
  > ping robotpi-34.enst.fr (ping 137.194.173.34)
### Connection via ssh
- personal hotspot  
  > ssh g7a@g7a.local 

- campus wifi  
  > ssh robotpi-34@robotpi-34.enst.fr
- password: g7a

### Logout
> logout


## Git
### creation of git repository on computer
to get the ssh key
>ssh-keygen -o -a 100 -t ed25519 -f .ssh/id_ed25519 -C "ruoxuan.yang@telecom-paris.fr"

### to set some parameters
>git config --global user.name "ruox"  
git config --global user.email "ruoxuan.yang@telecom-paris.fr"  
git remote add origin git@gitlab.enst.fr:proj103/2324/gr7/teama.git  
git config -l

### from computer to gitlab
to create a repository 
- go to the projet folder first
>git init

to check the git status
>git status 

to add documents
>git add

to commit
>git commit -m ""

to get documents from remote repository to local repository
>git pull origin main

to put documents from local repository to remote repository
>git push -u origin main (git push)

### from gitlab to Raspberry Pi
on the computer
>ssh-copy-id -i ~/.ssh/id_ed25519 git@robotpi-34

connect to Raspberry Pi
>ssh git@robotpi-34

get documents
>git clone git@gitlab.enst.fr:proj103/2324/gr7/teama.git
or
>git clone https://gitlab.telecom-paris.fr/proj103/2324/gr7/teama.git

- username: ruoxuan.yang
- password: Maggie0516

### enlever le mot de passe en utilisant ssh key or so
I basically just followed this: https://docs.gitlab.com/ee/user/ssh.html#generate-an-ssh-key-pair
- create key pair in ~/.ssh
- add the public key to gitlab
- add sth in the ~/.ssh/config file (as following in my case)
  >Host gitlab.com  
  >PreferredAuthentications publickey  
  >IdentityFile ~/.ssh/id_ed25519

### other
#### stash
- cf: https://segmentfault.com/a/1190000043631492

to stash
>git stash

to recover
>git stash pop

#### repeal
- cf: https://blog.csdn.net/w_p_wyd/article/details/126028094

repeal add 
>git reset

repeal commit
>git reset --soft HEAD^ 

repeal add+commit
>git reset --hard HEAD^



## flask
### app.py

#### @app.route('<\xxx>', methods=yyy)
- Routing: 定义了 URL 到特定视图函数的映射。当用户访问特定的 URL 时，Flask 将调用与之对应的视图函数来处理请求。
- URL（统一资源定位符）是用于定位互联网上资源的地址。它是指向网络上资源的标准地址格式，允许我们通过浏览器或其他应用程序访问网页、图像、文件或其他内容。    
ex. https://www.example.com:8080/path/to/resource?param1=value1&param2=value2#section2
  - 协议（Scheme）：定义了访问资源所使用的协议或规则，例如 http://, https://, ftp:// 等。
  - 域名或主机（Host）：指定了资源所在的主机名或 IP 地址，例如 www.example.com。
  - 端口（Port）：可选部分，指定了访问资源所使用的端口号，例如 :80。
  - 路径（Path）：指定了资源在服务器上的具体位置或路径，例如 /folder/file.html。
  - 查询参数（Query Parameters）：可选部分，包含在 URL 中以 ? 开头，用于向服务器传递额外的参数信息，例如 ?id=123&name=example。
  - 片段标识（Fragment Identifier）：可选部分，以 # 开头，用于定位页面中的特定部分，例如 #section1。
### templates
#### html
- 用于生成动态内容的 HTML 模板。Flask 使用模板引擎（如 Jinja2）来渲染模板，并将动态数据注入到 HTML 页面中。
- 使用 render_template() 方法渲染模板。
### static
- 在html中，可以通过 url_for('static', filename='file_name') 来引用静态文件。
#### js
- 
#### css



