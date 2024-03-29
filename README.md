# NewsRoom

## Description

NewsRoom is a web application designed to manage and publish news articles. It provides a user-friendly interface for administrators to create, edit, and organize articles, as well as manage categories, tags, menus, and blocks. The application also includes features for filtering articles by category and tag, implementing pagination for better navigation, and allowing external links in menus.

Features
Article Management: Create, edit, and delete news articles with rich text descriptions, publication dates, and associated categories and tags.
Category Management: Organize articles into categories with customizable logos and hierarchical structures.
Tagging System: Add tags to articles for better categorization and searchability.
Menu Management: Create custom menus with internal and external links, as well as dynamic links to categories.
Block Management: Configure blocks to showcase featured articles or specific content sections on the website.
Pagination: Implement pagination for browsing large collections of articles more efficiently.
Filtering: Filter articles by category and tag to find relevant content quickly.
User Authentication: Secure user authentication system for administrators to manage content.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tmetreveli/NewsRoom.git
   
2. Navigate to directory:
   cd NewsRoom/news_room
   
3. Install dependencies:
   pip install -r requirements.txt
   
4. Run migrations
   python manage.py makemigrations
   python manage.py migrate
   
5. create superuser to access admin page
   python manage.py createsuperuser
   
6. Run the development server:
   python manage.py runserver
   
7. Browse accessible api endpoints including:
   http://127.0.0.1:8000/admin, http://127.0.0.1:8000/api/articles, http://127.0.0.1:8000/api/categories, http://127.0.0.1:8000/api/menus/, http://127.0.0.1:8000/api/blocks
