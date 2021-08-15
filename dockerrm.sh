nodejs=`docker ps -aqf "name=nodejs"`
echo $nodejs
rediscache=`docker ps -aqf "name=rediscache"`
echo $rediscache
mongodb=`docker ps -aqf "name=mongodb"`
echo $mongodb

if [ -z "$nodejs" ]
then
      echo "No container available like nodejs"
else
      docker rm $nodejs -f
fi

if [ -z "$rediscache" ]
then
      echo "No container available like rediscache"
else
      docker rm $rediscache -f
fi

if [ -z "$mongodb" ]
then
      echo "No container available like mongodb"
else
      docker rm $mongodb -f
fi
