#!/usr/bin/env bash

# set -x

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



echo "Deploying to $DEPLOY_ENV"

# Set up paths needed for deploy
# See README for why we have to do this.
mkdir -p `echo $VIRTUAL_ENV `/lib/python3.6/site-packages/{pillow,libsass}

# Update Zappa
zappa update

# Migrate the Django DB
zappa manage $DEPLOY_ENV "migrate --noinput"

# Collect static files
zappa manage $DEPLOY_ENV "collectstatic --noinput"
