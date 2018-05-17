# searchgroup12
DD2476 Chatbot

#### ElasticSearch
	The familjeliv corpus can be imported into ElasticSearch by
	executing a PUT request at http://localhost:9200/familjeliv/_bulk
	with the data from the file qa-raw2.json. 
	This can be done using Postman by choosing PUT as the request type,
	binary as the body and the qa-raw2.json file, and setting the header to application/json

#### To use the virtual enviroment:
    cd ENV/bin/
    source activate
  
#### Django backend dev server:
    acivate virtual enviroment
    cd backend
    python manage.py runserver


#### React frontend dev server:
    cd frontend/chat-app
    npm install
    npm start
    then view web page at http://localhost:3000/
	
