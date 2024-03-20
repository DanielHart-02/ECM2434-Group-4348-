To run the Foodle web app:

1. Navigate to the directory of this README file in your terminal
2. With pip3 installed, run the commands:
   
   $ python3 -m venv .venv
   $ source myenv/bin/activate
   $ pip3 install -r requirements.txt

3. Change directory with the command:
   
   $ cd ecm2434_coursework/

4. Create a file named .env with the contents:
   
   EMAIL_USER = 'foodle.devteam@gmail.com'
   EMAIL_PASSWORD = '<Password provided in client docs>'

5. Start the web server with the command:

    $ python3 manage.py runserver

This will start the web server which should now be accessible through the link: http://127.0.0.1:8000/