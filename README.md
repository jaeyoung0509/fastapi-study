# FastAPI
> ## I referenced 
> - [Parwiz Forugh's youtube]<br>(https://www.youtube.com/watch?v=IZUjJ3rPY1E)
>- [fastapi offical document]<br>(https://fastapi.tiangolo.com/tutorial/middleware/) <br>
> -  [tortoise docuemnt]
> (https://tortoise-orm.readthedocs.io/en/latest/)
> - [fastapi - rabbitmq - celery]
>  https://medium.com/thelorry-product-tech-data/celery-asynchronous-task-queue-with-fastapi-flower-monitoring-tool-e7135bd0479f
> - db : postgress
> - backend : fastapi
> - orm : sqlalchemy(api, async_api) , tortoise
> - eidtor :vscode

### api folder:
>basic crud api using fastapi , sqlalchemy

### async_api folder:
> using async  , made a async api and jwt auth

### tortoise_orm folder:
> using tortoise_orm  not sqlalchemy ,  made a  async api

## pizza_api
> make relation between(order - user) using sqlalchemy  
> make CRUD async api  with fastapi  

## fastapi - rabbitmq - celery
> before using celery,  you need  message broker 
> instance rabbitmq(message broker) image with docker
> Celery is a distributed task queue that helps execute lots of processes/messages in the background asynchronously with real-time processing
> so if you have to do heavy works (like math operation, mail transmission) , celery is a good way 
