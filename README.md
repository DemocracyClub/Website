# Democracy Club website

This is the website hosted at https://democracyclub.org.uk/

## Set up
This is a Django project using PostgreSQL. The project is deployed using Python 3.6.

`pip install pipenv`

then 

`pipenv install`
## Blog Posts
To view blog posts, you need to first add new posts to your db. 
You can do this by creating an admin user in your terminal, then
navigating to the `/admin` panel to create a new post.

Blog posts now include tags which correspond to projects, such as
`representatives`. 
## Staging environment
Deploy to https://stage.democracyclub.org.uk to test/view edits
Once you have pushed your latest changes to your branch:

`git fetch origin` to get access to the development branch 
`git checkout development`
`git rebase master`
`git merge [YOUR BRANCH NAME]`
`git push origin development`

## DC Dependencies
- `[dc_django_utils]()` is the source code for basic HTML structure, forms
- `[dc_design_system]()` 

## Cron / scheduling / events

[TODO]
## Update docs to include 
- new pipeline settings
- Whitenoise