## djangozone


###Description

Open source blog from scratch written in Django.


###How the repository is organized

####Branches
This repository is organized in various branches which show different elements that combine together in the master branch (which is the working version of the djangozone.com page).

Example branches:

* Oauth: this branch shows what is needed to connect Django auth system with Oauth of various social services like Google, Facebook, Twitter, etc.
* DRF: this branch shows how to serve the data of your page as a REST API. Very useful if you want to connect your page with mobile, angularjs, famo.us and more.

####Commits
Each commit will have its correspondent blog posts if they are enough significative in their pertinent section/tag (oauth, drf, etc.). 

For example, in the oauth branch, in commit X I showed how to connect with Google oauth2 and you can find the related post [here](link). Obviously, minor modifications or bug fixes won't have a post itself but edits to the related post will be applied.


####Tags
Tags are directly related to stable commits. Oauth branch has its own tag which will be updated along with the branch when modifications are applied and bugs are fixed.


###Getting started

In order to start, follow this steps:

1. Download the commit you want to work with (the one reference in the post you are reading). `git clone https://github.com/argaen/djangozone.git;cd djangozone;git checkout <commit number>`. Use `git checkout 5fa3548` to download the scratch version to check the basics are working fine.

2. Install the needed dependencies: `sudo pip install Django`. If you don't have _pip_ installed, install it with your distribution package manager. _Ubuntu_: `sudo apt-get install python-pip`.

3. Go to `wsgi/openshift` folder and execute `python manage.py syncdb`. This will create the sqlite3 db file in the current folder.

4. You can start now the development server with `python manage.py runserver`. Check it is working in your browser, accessing [localhost](http://127.0.0.1/:8000) at port 8000. You should see a _Welcome home_ message if you downloaded the commit 5fa3548.

###Contributions

Comments, issues and others are always welcome =).
