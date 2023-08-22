#ssh root@120.26.195.153 'bash -s' < updateServer.sh
cd ~/touhou/Touhou-Emoticon-Database/
git fetch origin
git merge origin/server
