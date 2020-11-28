# read input param
if [ -n "$1" ] ; then reposityName=$1; else echo -e "usage:\n\t./build.sh reposityName [tagName]" && exit 1 ;  fi
if [ -n "$2" ]  && [ "$2" != "master" ] ; then tagName=$2; else tagName="latest" ; fi
imageName=$reposityName:$tagName # $tagName:"$(date +%Y%m%d)"

# docker build -f Pre.Dockerfile -t ml_platform_python:pre  . 
echo "====== build docker image:$imageName ===="
docker build -t $imageName .
imageName2=$imageName
docker tag $imageName $imageName2
echo "===> push image to private registry "
docker push $imageName2



