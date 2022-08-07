# Codestar
  Codestar is the blogpost website made for the educational purposes.
  This website is created for the users who love social media. In this blogweb website, there 
  are a lot of functionalities for the users like, users can create the posts with the images, can 
  add or read the post, edit or update the post, delete the post,
  can like the post and can leave a comment on the post.

The deployed link can be found here: [Live Site](w/)

# Table of contents
  * [Users stories](#users-stories)
  * [Features](#features)
  * [Agile technique](#agile-technique)
  * [Features left to implement](#features-left-to-implement)
  * [Validator testing](#validator-testing)
  * [Technology Used](#technology-used)
  * [Libraries & Integrations](#frameworks-libraries-and-programs)
  * [Project visualization](#project-visualiztion)
  * [Wireframe pic](#wireframe-pic)
  * [Deployment](#deployment)
  * [Credits](#credits)

# Users stories:
  * As a user I can read the post
  * As a user I can create the post
  * As a user I can edit or update the post
  * As a user I can delete the post
  * As a user I can like the post
  * As a user I can comment on the post

# Features
    *Header:
            *The navigation bar is present at the top of every page and includes all links to the various other pages.
            *The My Account navigation link is a drop down menu which includes the Sign up and Log in links.
            *When the user has logged in, the My Account drop down menu changes to display the user's name and a profile icon.
            *Users can add post and logout using the links showing on the navbar.
            [Header](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/header.png)
            [login](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/login.png)
    * Sign Up:
            * Users can register their account by clicking on the sign up button showing
            on the navbar.
            [signup](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/signup.png)
    * signin:
            * Users can signin by clicking on the button showing on the navbar so that they can enjoy the functionalities of the website. Users can only create, edit and delete    the post by registering their account on the website.
            [signin](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/signin.png)
    * Add the post:
            * Users can create the posts along with uploading images
            * steps to create the posts are as below
            * First put the title in the title field for your post.
            * Put the title tag for your post in the slug field.
            * You can add the content for your post and style it using the editor showing
            in the content field.
            * You can also upload the image using the upload image field for your post.
            [add post](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/Add%20post.png)
    * Admin panel:
            [admin](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/admin_panel.png)
    * Comment
            * Users can comment on the post.
            [comment](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/comment.png)
    * Edit or Update the post:
            * Users can edit or update the post by clicking on the edit button showing below 
            the image of the post.
            [edit or update](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/edit%20post.png)
    * Delete the post:
            * Users can delete the post by clicking on the delete button showing below the
            image of the post.
            * Users cannot delete the others post.
            [delete](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/delete%20post.png)
    * Footer:
            * Footer displays the social link and purpose of post.
            [footer](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/footer%20page.png)

# Agile technique:
  * Agile technique is used in this project. You can have a look here
    [Agile](https://github.com/surba778/DjangoBlog/issues)

# Features left to implement
  * I will add the user profile with image upload option in the future for the users who create 
  the account and also edit profile option so they can edit the profile.

# Testing
    ## User story testing
        * As a site user i can register an account so that i can add/edit/delete my post and comment on the post and also add the post.
        * A sign up button is immediately visible on the landing page as a call to action for the user to sign up to get started. When the user clicks the button they are taken to the sign up page.
        * Once the user has registered an account they can perform all the actions.
        * As a Site User, I can login or logout of my account so that I can keep my account secure. If the user has registered an account they can access the login and logout buttons in the Navbar. As a Site User I can see my login status so that I know if I'm logged in or out.
    ## User Navigation
        * As a User I can immediately understand the purpose of the site.
        * As a Site User, I can view a paginated list of posts so that I can select a post to view. Also if a user click on a post then user can read the full comment and post.
        * As a Site User, I can view my posts so that I can see and manage all posts. 
    ## Browser testing
        * The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.
# Validator Testing
   I have manually tested this project by doing the following:
   * Passed the code through a PEP8 linter and confirmed there are no problems
   * PEP8
     * No errors were returned from [PEP8 checker](http://pep8online.com/)
        (https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/pep8.png)
   * Html checker:
     * No errors were returned from [W3C Html](https://validator.w3.org/)
   * CSS checker:
     * No errors were returned from [W3C CSS](https://jigsaw.w3.org/css-validator/)
        (https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/css_validator.png)
   * JS checker:
     * No errors were returned from [JS HINT](https://jshint.com/)
        (https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/jshint_validation.png)
   * Accessiblity:
     * I confirmed that colours and font chosen are easy to read and accessible by running it through lighthouse
     in devtools.
     * Generated report is here below.
        (https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/lighthouse.jpg)
  
# Technology Used 
  * [Html](https://en.wikipedia.org/wiki/HTML)
  * [Css](https://en.wikipedia.org/wiki/CSS)
  * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * [Boostrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
  * [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [GitHub](https://github.com)
  * [Gitpod](https://www.gitpod.io)
  * [Heroku](https://en.wikipedia.org/wiki/Heroku)

# Libraries & Integrations
- [Django](https://www.djangoproject.com/)
    - Used as the primary framework to build the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to render the forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Used for user authentication on the site.
- [Django Countries](https://pypi.org/project/django-countries/)
    - Used to populate the countries select field on the order form and profile form.
- [Coverage](https://pypi.org/project/coverage/)
    - Used to produce a testing report.
- [Stripe](https://stripe.com/gb)
    - Used to handle payments.
- [Bootstrap](https://getbootstrap.com/)
    - Used as a framework for styling and to make the site responsive via grid system.
- [Amazon Web Services](https://aws.amazon.com/)
    - Used to store static files and images.
- [SQLite](https://www.sqlite.org/index.html)
    - Database used in development.
- [PostgreSQL](https://www.postgresql.org/)
    - Database used in production.
- [Heroku](https://id.heroku.com/login)
    - Online Cloud Platform used to deploy the live site.
- [Gunicorn](https://gunicorn.org/)
    - Used for deploying the project to Heroku.
- [Fontawesome](https://fontawesome.com/)
    - Used for icons across the website. 
- [Google Fonts](https://fonts.google.com/)
    - Used to import "Roboto" & "Mrs Saint Delafield" fonts used across the website. 
- [jQuery](https://jquery.com/)
    - Used to simplify JavaScript code. 
- [Github](https://github.com/)
    - Used to store the project code after being pushed from Git.
- [Git](https://git-scm.com/) 
    - Used for version control to commit to Git and Push to GitHub.

# Project visualization diagram:
   [Visualization](https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/database_schema.png) 

# Wireframe pic
    (https://github.com/surba778/DjangoBlog/blob/main/docs/readme_images/features/wireframe%20blog.jpg)

# Deployment

## Set up project locally

First, ensure the following are set up on your IDE:
- [PIP3](https://pypi.org/project/pip/) Python package installer. 
- [Python 3.8](https://www.python.org/downloads/release/python-360/) or higher.
- [Git](https://git-scm.com/) version control.

To clone the project up locally you can follow the following steps: 

1. Navigate to the repository - [Repository](https://github.com/surba778/DjangoBlog)

2. Click the code dropdown button and copy the url. 

3. Open the terminal in your IDE and enter the following code: 
    - ```
        git clone https://github.com/surba778/DjangoBlog.git
        ```

4. Install the dependencies needed to run the application by typing the following command into the terminal: 
    - ```
        pip3 install -r requirements.txt
 

5. Set up the environment variables: 
    
    - Inside the env.py file add the following code:
        - ```
            import os

            os.enviorn["DATABASE_URL"] = "your database url"
            os.environ["SECRET_KEY"] = "Your secret key"
            os.environ["CLOUDINARY_URL"] = "Your cloudinary url"
            

6. To set up the database migrate the database models by typing the following commands into the terminal: 
    - ```
        python3 manage.py showmigrations
        python3 manage.py makemigrations
        python3 manage.py migrate
        
7. Create a superuser to have access to the django admin dashboard type the following commands into the terminal:
    - ```
        python3 manage.py createsuperuser
        ```
    - Then set up the account by adding your username, email and password. 

8. Finally, run the app locally by typing the following command into the terminal: 
    - ```
        python3 manage.py runserver
        ```


## Deploy to Heroku

1. Create a Heroku app: 
    - Go to [Heroku](https://www.heroku.com/) and create an account if you do not have one yet. 
    - From the dashboard click on 'new app' button, name your app and choose the region closest to you. 
    - On the resources tab set up a new Postgres database by searching for 'Postgres'.
2. On your IDE, install 'dj_database_url' & 'psycopg2' to enable the use of the Postgres database: 
    - In the terminal type the following commands:
        - ```
            pip3 install dj_database_url
            pip3 install psycopg2-binary
            ```
3. Add the downloaded dependencies to the requirements file:
    - ```
        pip3 freeze > requirements.txt
        ```
4. To setup the new database go to to settings.py, import 'dj_database_url', comment out the default database configuration and replace the default database with the following: 
    - ```
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.parse("The URL of your Heroku Postgres database")
        }
        ```
5. Run all migrations to the new Postgres database by entering the following command in the terminal:
    - ```
        python3 manage.py migrate
        ```
6. Create a superuser by typing the following command into the terminal:
    - ```
        python3 manage.py createsuperuser
        ```
    - Then set up the account by adding your username, email and password. 
7. In settings.py set up the following to use the Postgres database when the app is running on Heroku and the SQLite3 when the app is running locally:
    - ```
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        ```
8. Install Gunicorn (which will act as our webserver) by typing the following commands into the terminal:
    - ```
        pip3 install gunicorn
        pip3 freeze > requirements.txt
        ```
9. Type the following into the procfile: 
    - ```
        web: gunicorn restaurant.wsgi
        ```
10. Log in into the Heroku terminal:
    - ```
        heroku login -i
        ```
11. Disable collectstatic to prevent Heroku from collecting static files when deployed, by typing the following command into the terminal: 
    - ```
        heroku config:set DISABLE_COLLECTSTATIC=1 --app "heroku_app_name"
        ```
12. In settings.py add the hostname of the Heroku app, and allow localhost: 
    - ```
        ALLOWED_HOSTS = ['"heroku_app_name".herokuapp.com', 'localhost']
        ```
13. Deploy to Heroku by typing the following commands into the terminal: 
    - ```
        heroku git:remote -a "heroku_app_name"
        git push heroku main
        ```
14. To set up automatic deployments in Heroku when pushing code to github:
    - On the deploy tab, connect to github by searching for the repository name and clicking 'Connect'.
    - Click 'Enable Automatic Deploys" 
15. Generate a django secret key at [Djcrety](https://djecrety.ir/) and add it to 'Settings' > 'Config variables' in Heroku.
16. Update the settings.py file to collect the secret key from the environment, and use an empty string as default: 
    - ```
        SECRET_KEY = os.environ.get('SECRET_KEY', '')
        ```
17. Set debug to be true only if there's a variable called "DEVELOPMENT" in the environment. 
    - ```
        DEBUG = 'DEVELOPMENT' in os.environ
        ```


# Credits

## Code

- [Code Institute](https://codeinstitute.net/): for git template IDE and heroku deployment instructions. The Idea of README.md file and the codes used for the website were also learnt from Code Institute.

- [Django course](https://www.youtube.com/watch?v=PtQiiknWUcI): This youtube walkthrough help me to learn about Django.

- [Codemy.com](https://codemy.com/) Few codes were also learnt from codemy.

- [Stack Overflow](https://stackoverflow.com/) Few codes were also learnt from stack overflow.

- [pexels](https://www.pexels.com/) The best free stock photos.

## Media
   - Cloudinary is used in this project for images purposes.

## Acknowledgement
- Mentors help and advice
- Tutors help