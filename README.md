# Projeto FLask usando Celery e Redis

Rodando

```bash
$ docker-composer up -d
``` 


```bash
celery worker -A app.celery --loglevel=info
``` 