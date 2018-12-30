Logs Analysis
===

Description
---
Analysis of articles with authors and track of logs of the articles.
---
Author
---
Brian Shen
---
Setup
---

The program requires vagrant, python 3, postgresql, and the dataset.

*To install vagrant* 
1. Follow the link below to the download the appropriate package.
https://www.vagrantup.com/downloads.html
2. After downloading vagrant packagem, place the file where you want the virtual machine to be. Then run the code below.
```
vagrant up
```
3. After vagrant has installed, you can now connect to the virtual machine by running the code below.
```
vagrant ssh
```

*To install python 3 on Linux server*
```
sudo apt install python3-pip
```

*To install postgresql*
```
sudo apt-get install postgresql
```

*To install the dataset*
1. download the data set from the link below
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

2. Once the file is downloaded place the file in the same folder where you placed the vagrant virtual machine. 
Then run the code below in your vagrant VM.
```
psql -d news -f newsdata.sql
```
---

Running the script
---
The script is written in python 3. Import the python script to your VM, then run the code below.
```
python logsanalysis.py
```

