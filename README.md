# Evident-BD-Ltd
1. Clone the repository:
   ```sh
   git clone https://github.com/subreto-roy/Evident-BD-Ltd.git
   cd AmiCodingPariNa/
   ```



2. Install the project dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Perform database migrations:
   ```sh
   python manage.py migrate
   python manage.py makemigrations
   ```

4. Create a superuser account:
   ```sh
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```sh
   python manage.py runserver
   ```

after that  you need to this url
http://127.0.0.1:8000/khuj/
first you need to sign up then you can search the value.

Token Based API:
first you need to run this url
http://127.0.0.1:8000/api/
you need to create a token in database 
than run tha main.py and give the Token number.

Session Based API:
First you need to log in then run this url
http://127.0.0.1:8000/seasion_history_api/
