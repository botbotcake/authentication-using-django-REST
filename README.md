# authentication-using-django-REST

1)Install the requirements using
  pip install -r requirements.txt


2)Set up initial migration

 python manage.py makemigrations
 
 python manage.py migrate
 
 python manage.py createsuperuser
 
 python manage.py runserver


3)End points

login - http://127.0.0.1:8000/api/v1/rest-auth/login/
all users - http://127.0.0.1:8000/api/v1/users
logout - http://127.0.0.1:8000/api/v1/rest-auth/logout/
register - http://127.0.0.1:8000/api/v1/rest-auth/registration/

4)Install Postman for firing request
    
    i)To check the list of registered users
      Method= GET |  url = http://127.0.0.1:8000/api/v1/users
      
      Example 
      [
            {
                "email": "",
                "username": "admin"
            },
            {
                "email": "",
                "username": "TestUser"
            }
        ]


    ii) To register
      Method = POST | url = http://127.0.0.1:8000/api/v1/rest-auth/registration/
      
      Body = 
                {
              "username": "",
              "email": "",
              "password1": "",
              "password2": ""
                }
                
     
     iii)To login
          Method = POST | url = http://127.0.0.1:8000/api/v1/rest-auth/login/
     
                {
                      "username": "",
                      "email": "",
                      "password": ""
                  }
                  
                  
     iv) To logout
      Method = POST | url = http://127.0.0.1:8000/api/v1/rest-auth/logout/
     
     
               
