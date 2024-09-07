# Memories-store
 This project having some features like- Login ,Signup , Image-upload, Search user uploaded images.
#Run instructions--
   # Django Project
1.
## Requirements
Before you can run this project, ensure you have the following installed:

- Python 3.x
- Django (version used in this project)
- Virtualenv (optional but recommended)
- Pillow

## Setting Up the Project Locally

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/your_username/your_django_project.git
cd your_django_project
2.
  #Create virtual environment 
   # On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

3. Install all requirements 

4. Setup Environment variables 
  SECRET_KEY='your-secret-key'
DEBUG=True
DATABASE_URL='sqlite:///db.sqlite3'

5.Apply database migration
  python manage.py makemigrations 
  python manage.py migrate

6.Create a superuser (optional)
  python manage.py createsuperuser

7.Run the server 
  python manage.py runserver
 
8. Copy the link and search in any browser

Website overview-
At first , there is a Login page . If anyone already have account then they can log in.
 Otherwise there is a Sign-up button , they have to click and go to the Sign-up page and create their account.
 After logged in , the image-upload page will be open. There loggedin user can upload image and see their previously uploaded images.
 In that page SearchUser and Logout option also their.
 If anyone click SearchUser page then open a search user page where the user can search any other user's photos by their name.
 And if click Logout option then that user will be Logged out and redirect to the Login page.
 

