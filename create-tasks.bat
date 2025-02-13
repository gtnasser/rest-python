curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Create party list\"}" http://127.0.0.1:5000/task
curl -X POST -H "Content-Type: application/json" -d "{\"done\":\"True\", \"title\":\"Get Ice Cream\"}" http://127.0.0.1:5000/task
curl -H "Content-Type: application/json" http://127.0.0.1:5000/task
