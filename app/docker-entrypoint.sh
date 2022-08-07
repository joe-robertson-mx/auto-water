#!/bin/sh
set -e
sleep 10
echo Checking migrations
if [ ! -f "./migrations/env.py" ]
then
  echo Migrating DB
  flask db init
  flask db migrate -m "Init"
  flask db upgrade
  flask run
else
  echo Migration found
  flask db migrate -m "Init"
  flask db upgrade
  flask run
fi

###WHYS THIS RUNNING MULTIPLE TIMES
# gunicorn -c gunicorn.config.py wsgi:app

  #!/bin/sh
  
# until flask db upgrade
# do
#     echo "Waiting for postgres ready..."
#     sleep 2
#     flask db init
#     flask db migrate -m 'create initial tables'  # this might be a not-great idea, now that i look at it again
# done