ssh root@120.26.195.153 'bash -s' < ./serverScript/dbSnapshot.sh
git fetch origin
git checkout server
git merge origin/server
