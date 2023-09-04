#ssh root@120.26.195.153 'bash -s' < dbSnapshot.sh
cd ~/touhou/Touhou-Emoticon-Database/
mysqldump -u root -p343542 --skip-extended-insert Touhou pics_pictures > dbSnapshot.txt
git add .
git commit -m "update database"
git push -u origin server
