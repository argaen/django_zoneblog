## djangozone


###Description

Open source blog from scratch written in Django.


###How the repository is organized

####Branches
The repository is organized in various branches which show different elements that combine together in the master branch (which is the working version of the [django.zone](http://django.zone) page).

Example branches:

* **master**. Main branch. Contains the code of the current blog version.
* **development**. Branch where all commits and modifications are performed. It will be merged to master branch when a new important functionality is added.
* **Oauth**. This branch (will) shows what is needed to connect Django auth system with Oauth of various social services like Google, Facebook, Twitter, etc.
* **DRF**. This branch (will) shows how to serve the data of your page as a REST API. Very useful if you want to connect your page with mobile, angularjs, famo.us and more.

####Commits
Each commit will have its correspondent blog post if it is enough significative in its pertinent section/tag (oauth, drf, etc.). 

For example, in the master branch, in commit b72889d I released this blog and you can find the related post [here](http://django.zone/posts/1). Obviously, minor modifications or bug fixes won't have a post itself but edits to the related post will be applied.


###Getting started

In order to start, follow this steps:

1. Download the commit you want to work with (the one referenced in the post you are reading). `git clone https://github.com/argaen/djangozone.git;cd djangozone;git checkout <commit number>`. Use `git checkout 5705de9` to download the scratch version to check the basics are working fine.

2. Install the needed dependencies: `sudo pip install Django`. If you don't have _pip_ installed, install it with your distribution package manager. _Ubuntu_: `sudo apt-get install python-pip`.

3. Go to `wsgi/openshift` folder and execute `python manage.py syncdb`. This will create the sqlite3 db file in the current folder.

4. You can start now the development server with `python manage.py runserver`. Check it is working in your browser, accessing [localhost](http://127.0.0.1/:8000) at port 8000. You should see a blank page if you downloaded the commit 5705de9. 

5. If the previous step worked, now execute `git checkout 315807d05d`, remove the sqlite3 file, and repeat the previous steps. Now you should see an exact copy of the blog without any posts. User and password for the admin is admin-123.

###Contributions

Comments, issues and others are always welcome =).
