# CC_assignment_2

* Ideas :-

* Network Proxy :- /etc/enviornment
  - http_proxy="http://wwwproxy.unimelb.edu.au:8000"
  - https_proxy="http://wwwproxy.unimelb.edu.au:8000"
  - ftp_proxy="http://wwwproxy.unimelb.edu.au:8000"
  - no_proxy=localhost,127.0.0.1,127.0.1.1,ubuntu

* Installing Nodejs-
  1. wget https://nodejs.org/en/blog/release/v6.0.0/
  2. tar -xf <file_name>
  3. Configure PATH in ~/.bash_profile
    - export PATH=/home/ec2-user/node-v6.0.0-linux-x64/bin:$PATH
    
* Resolving docker and proxy issues
  - https://www.youtube.com/watch?v=P0W_LhBjDgI
  - https://www.youtube.com/watch?v=hDuyvdzLWlo
  
* Installing CouchDB
  1.  yum -y install epel-release
  2.  cd /etc/yum.repos.d/
    2.1. vi apache-couchdb.repo
    2.2. ADD:
         [bintray--apache-couchdb-rpm]
         name=bintray--apache-couchdb-rpm
         baseurl=http://apache.bintray.com/couchdb-rpm/el$releasever/$basearch/
         gpgcheck=0
         repo_gpgcheck=0
         enabled=1
  3- yum -y install couchdb
  4- systemctl start couchdb
  5- cd /opt/couchdb
    5.1- vi etc/default.ini
    5.2- CHANGE:
         [chttpd]
         port = 5984
         bind_address = 0.0.0.0
  6- systemctl restart couchdb
  
* Port forwarding - ssh -i ./sins101.pem -N -L 5984:localhost:5984 ec2-user@172.26.38.5
