# Democracy Club website

This is the website hosted at https://democracyclub.org.uk/

## Set up

This is a Django project using PostgreSQL. The project is deployed using Python 3.6.

Use by setting up a `virtualenv` and install packages using `pip install -r requirements/production.txt`.

For local and testing environments use `pip install -r requirements/testing.txt`.

## Deploying with Zappa

This site is deployed to AWS Lambda using [Zappa][zappa].

To deploy the site you must have an AWS account with permissions to write to the lambda function, S3 bucket, etc.

Zappa is expecting a the config for this AWS account to be in a profile file at `~/.aws/credentials`. The profile name must be `dc`.

```
[dc]
aws_access_key_id = XXXXXXXXX
aws_secret_access_key = XXXXXXXXX
region = eu-west-2
```

Zappa requires an active, local virtualenv. It's best to make one for production and one for local dev. A production env will be smaller and wont deploy all the testing packages.

To deploy:

* `export AWS_PROFILE=dc`
* `deploy.sh [dev|prod]`

This will:

1. Make empty directories in the virtualenv for some wheels. This is a hack to get around a bug in zappa. Basically zappa tried to install wheels from pypi rather than from the vifrtualenv, if the package is arch dependant. Sometimes it fails to detect this and creating an empty directory forces it to install them. This applies to Pillow and libscss.
2. runs `zappa update`
3. Migrates Django and collects static

If the build fails, run `zappa tail [dev|prod] --since SINCE` to [tail the log](https://github.com/Miserlou/Zappa#tailing-logs) and debug the build.

## Cron / scheduling / events

See the `events` key in `zappa_settings.json`.

Commands are run using the hacky `zappa_commands.py` file – see there for more.

[zappa]: https://github.com/Miserlou/Zappa
