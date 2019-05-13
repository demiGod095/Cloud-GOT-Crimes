# CC_assignment_2

* Ideas :- We are doing GOT

* Network Proxy :- /etc/enviornment
  - http_proxy="http://wwwproxy.unimelb.edu.au:8000"
  - https_proxy="http://wwwproxy.unimelb.edu.au:8000"
  - ftp_proxy="http://wwwproxy.unimelb.edu.au:8000"
  - no_proxy=localhost,127.0.0.1,127.0.1.1,ubuntu

* To install Python
  - Getting your Server ready for the install:
     - sudo yum update
     - sudo yum install yum-utils
     - sudo yum groupinstall development
     - sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm



  - Installing Python and PIP
     - sudo yum -y install python36u
     - python3.6 -V
     - sudo yum -y install python36u-pip
     - sudo yum -y install python36u-devel


* Installing Nodejs-
  1. wget https://nodejs.org/en/blog/release/v6.0.0/
  2. tar -xf <file_name>
  3. Configure PATH in ~/.bash_profile
    - export PATH=/home/ec2-user/node-v6.0.0-linux-x64/bin:$PATH
    
* Resolving docker and proxy issues
  - Refer Docker-README.md
  
* Installing CouchDB
  - yum -y install epel-release
  - cd /etc/yum.repos.d/
    - vi apache-couchdb.repo
    - ADD:
         [bintray--apache-couchdb-rpm]
         name=bintray--apache-couchdb-rpm
         baseurl=http://apache.bintray.com/couchdb-rpm/el$releasever/$basearch/
         gpgcheck=0
         repo_gpgcheck=0
         enabled=1
  - yum -y install couchdb
  - systemctl start couchdb
  - cd /opt/couchdb
    - vi etc/default.ini
    - CHANGE:
         [chttpd]
         port = 5984
         bind_address = 0.0.0.0
  - systemctl restart couchdb
  
* Port forwarding - ssh -i ./sins101.pem -N -L 5984:localhost:5984 ec2-user@172.26.38.5
