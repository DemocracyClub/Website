# Democracy Club website

This is the website hosted at https://democracyclub.org.uk/

## Set up
This is a Django project using PostgreSQL. The project is deployed using Python 3.6.

### Packages
This project uses pipenv to manage dependencies. 
To perform the package install, run the following within your venv:
```commandline
pip install pipenv
pipenv install
```
Read more about pipenv package management [here](https://pipenv.pypa.io/en/latest/).

### Database
First, ensure you have Postgres available. 
```commandline
#OSX
brew install postgres
```
You'll then need to create a database for this project.
```
createdb democracy_club
```
Once you're st up, run the migration:
```commandline
python manage.py migrate
```


## Blog Posts
To view blog posts, you need to first add new posts to your db. 
You can do this by creating an admin user in your terminal
```
python manage.py createsuperuser
```
then navigate to the `/admin` panel to create a new post.
New posts are created at `/admin/hermes/post`.


Blog posts now include tags which correspond to projects, such as
`representatives`. 

We've hard-coded tags to reduce the risk of typos and to ensure that tags are used consistently. To add or edit a tag, change the `tag_values` variable in `democracy_club/apps/hermes/admin.py`.

## Staging environment
Add your branch to the staging env on .circleci/config to deploy to https://stage.democracyclub.org.uk and test/view edits

## DC Dependencies
- `[dc_django_utils]()` is the source code for basic HTML structure, forms
- `[dc_design_system]()` 

## Cron / scheduling / events

# Deployment

This project is deployed using CircleCI.

Pages are normally cached using CloudFront, and a site-side invalidation is
created on each new deployment.

[TODO]
## Update docs to include 
- new pipeline settings
- Whitenoise
