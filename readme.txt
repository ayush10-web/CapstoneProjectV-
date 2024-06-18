docker network create test-net  
docker build -t test-frontend ./Frontend 
docker build -t test-backend ./Backend 
docker run -d -it -p 8080:8501 --network test-net --name frontend-container test-frontend
docker run -d -it -p 5000:5000 --network test-net --name backend-container test-backend  


docker pull rujalmhn/aiback:1.0
docker pull rujalmhn/aifront:1.0
docker network create mynetwork
docker run -d --name aiback-container --network mynetwork -p 5000:5000 rujalmhn/aiback:1.0
docker run -d --name aifront-container --network mynetwork -p 8501:8501 rujalmhn/aifront:1.0


docker pull composer/composer
docker-compose up -d
docker-compose ps