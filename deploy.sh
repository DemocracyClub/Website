#!/usr/bin/env bash
set -e

die () {
    echo >&2 "$@"
    exit 1
}

if [ $# -eq 0 ]
  then
    die "No env supplied. Call with ./deploy [dev|prod]"
fi


DEPLOY_ENV=$1
[ $DEPLOY_ENV == "dev" ] || [ $DEPLOY_ENV == "prod" ] || die "Env not valid. Must be dev or prod"
export STAGE=$1

echo "Performing Django checks"
FRAMEWORK="Zappa" python manage.py check

echo "Running collectstatic locally to check for errors"
FRAMEWORK="Zappa" python manage.py collectstatic --noinput

echo "Deploying to $DEPLOY_ENV"

# Set up paths needed for deploy
# See README for why we have to do this.
mkdir -p `echo $VIRTUAL_ENV `/lib/python3.6/site-packages/{pillow,libsass}

# Update Zappa
zappa update $DEPLOY_ENV

# Migrate the Django DB
zappa manage $DEPLOY_ENV "migrate --noinput"
