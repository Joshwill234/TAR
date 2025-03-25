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

## Development Process

Project Management & Issue Tracking
GitHub Issues for Development Documentation
The development process was documented using GitHub Issues, providing a structured approach to tracking tasks and progress. Two issue templates were created to standardize reporting:

User Stories – Detailed breakdowns of specific tasks.
Account registration: As a Site User I can register an account so that I can comment on a post.

**Acceptance Criteria**

1 Given an email a user can register an account.
2 Then the user can log in.
3 When the user is logged in they can comment.




View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation

**Acceptance Criteria**

1 Given one or more user comments the admin can view them.
2 Then a site user can click on the comment thread to read the conversation.


Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation

**Acceptance Criteria**

1 When a user comment is approved
2 Then a user can reply
3 Given more than one comment then there is a conversation thread


Open a post: As a Site User, I can click on a post so that I can read the full text.

**Acceptance Criteria**

1 When a blog post title is clicked on a detailed view of the post is seen.


Modify or delete comment on a post: As a Site User I can modify or delete my comment on a post so that I can be involved in the conversation


**Acceptance Criteria**

1 Given a logged in user, they can modify their comment
2 Given a logged in user, they can delete their comment

Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content


**Acceptance Criteria**

1 Given a logged in user, they can create a blog post
2 Given a logged in user, they can read a blog post
3 Given a logged in user, they can update a blog post
4 Given a logged in user, they can delete a blog post

Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later


**Acceptance Criteria**

1 Given a logged in user, they can save a draft blog post
2 Then they can finish the content at a later time

Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments


**Acceptance Criteria**

1 Given a logged in user, they can approve a comment
2 Given a logged in user, they can disapprove a comment


To improve visibility, issues were categorized with labels such as:

Bugs – Tracking and fixing defects.

User Epics – Major features and milestones.

User Stories – Smaller, actionable development tasks.

Style – UI/UX improvements and design refinements.

MoSCoW Prioritization
The MoSCoW method was applied to classify issues based on priority:

Must-Have – Essential features required for functionality.

Should-Have – Important but not critical enhancements.

Could-Have – Optional improvements that enhance user experience.

Sprint Planning & Kanban Workflow
Development was structured into sprints, managed via GitHub Projects, which provided a Kanban board for tracking issue progress. Tasks moved through the following stages:

To Do – Planned work awaiting implementation.

In Progress – Features currently under development.

Done – Completed and reviewed tasks.

The project was executed in three iterations, each focusing on key development phases:

Iteration 1 – Core feature implementation.

Iteration 2 – Refinements, bug fixes, and improvements.

Iteration 3 – Final enhancements and optimizations.

## Wireframes

![image](https://github.com/user-attachments/assets/42e62b53-36c6-4fd6-9481-d97d79006d45)
![image](https://github.com/user-attachments/assets/05956ab5-e148-4d65-96fb-c69d546d6291)
![image](https://github.com/user-attachments/assets/44ec1553-f5aa-446f-95aa-79c12f8e44fd)



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

This README file provides an overview of the project, including its features, installation instructions, usage, project structure, models, views, templates, and acknowledgements. 
