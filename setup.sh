
# local testing 
docker build -t fastapi .
docker run -d --name fastapi-container -p 8080:8080 fastapi