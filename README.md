# Flask com Celery e Redis

How to run project

```bash
$ docker-composer up -d
``` 


```bash
celery worker -A app.celery --loglevel=info
``` 
