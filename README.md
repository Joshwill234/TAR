# Tasty African Recipes

Tasty African Recipes is a Django-based web application that allows users to browse, like, and comment on various African recipes. The project includes features such as user authentication, post liking, commenting, and a carousel for showcasing images.

## Features

- User authentication (login, logout, signup)
- Browse and view recipes
- Like and unlike recipes
- Comment on recipes
- Edit and delete comments
- Carousel for showcasing images

## Usage

### Home Page
The home page displays a carousel with images and a list of recipes. Each recipe includes the title, excerpt, author, and creation date. Users can click on a recipe to view the full details.

### Recipe Details
The recipe details page displays the full content of the recipe, along with the number of likes and comments. Users can like or unlike the recipe and add comments.

### User Authentication
Users can sign up, log in, and log out using the authentication system provided by Django Allauth.

### Liking Recipes
Authenticated users can like or unlike recipes. The like button is displayed on the recipe details page.

### Commenting on Recipes
Authenticated users can add comments to recipes. Users can also edit or delete their own comments.

## Models
![image](https://github.com/user-attachments/assets/b6b27fa7-501b-4f11-aa53-766acce273c7)



## Templates

### index.html
The index.html template displays the list of recipe posts and the hero carousel.

### post_detail.html
The post_detail.html template displays the details of a recipe post, including comments and likes.

### base.html
The base.html template is the base template for the project, including the navigation bar and footer.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Django
Bootstrap
Font Awesome
Django Allauth

This README file provides an overview of the project, including its features, installation instructions, usage, project structure, models, views, templates, and acknowledgements. You can customize it further based on your specific project details.
