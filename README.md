# simple-blog

A simple bootstrapified django blog featuring comments and user authentication.

## Features
- User Authentication: Users can register and login to the site. They can view and add comments to posts (which can only be made by superusers.)
- Posts: Superusers can create, edit, comment, and delete posts.
- Comments: Any users can add comments within a post.

## How to Run it Locally
1. Install virtualenv:

    ```bash
    pip install virtualenv
    ```
    
2. Navigate to the API directory and create a virtual environment there:
 
    ```bash
    virtualenv [INSERT_NAME]
    ```
    
3. Run the virtual environment:
 
    ```bash
    source [NAME]/Scripts/activate
    ```
    
 
4. Install django and django-ckeditor within the virtual environment:
 
    ```bash
    pip install django
    pip install django-ckeditor
    ```
5. Create a superuser:
 
    ```bash
    winpty python manage.py createsuperuser
    ```
    
6. Run the server. Then you can access it on http://localhost:8000/:
    ```bash
    python manage.py runserver
    ```
7. Go to http://localhost:8000/admin/auth/user/ and select the superuser you made before. Insert First Name and Last Name. Click Save.
    
    
    
    
    
