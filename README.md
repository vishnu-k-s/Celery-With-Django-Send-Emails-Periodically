

                      CELERY WITH DJANGO TO SEND EMAIL PERIODICALLY


OVERVIEW

        This django project demonstrate how to use celry with django to send emails periodically

SETUP

        * Install django, celery, celery beat, redis
        * Add configrations to 
                    settings.py -> celery settings, email settings 
        * Create files 
                    celery.py, __init__.py, tasks.py
        * To celery to work
                    call task function in views.py 

        * To create schedules dynamically
                    in views.py add new end point

HOW TO RUN

        * Run django server
    
        * Run celery worker
    
            celery -A celery_project.celery worker -l info

        * Run celery beat


