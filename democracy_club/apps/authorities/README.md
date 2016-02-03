
## Bootstrapping

install this Django project in the normal way.

### Accounts

For the member function you'll need some Social Auth account from Facebook and Twitter.

### Authorities and EveryElection

First import Authorities:

> ./manage.py import_authorities

Then import the local services from local.direct.gov:

> ./manage.py import_local_services

Then import the sub-areas we care about from MaPit:

> ./manage.py import_mapit_area_type

For the 2015 local elections, import them from the Google doc:

> ./manage.py import_local_elections
