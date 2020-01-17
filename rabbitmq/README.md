# RabbitMQ

1. In docker for local testing:

    docker run -d --rm --name some-rabbit -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq

2. Enable the management plugins:

    docker container exec -it some-rabbit rabbitmq-plugins enable rabbitmq_management

3. View the administrator GUI: http://localhost:15672 

* Username: guest
* Password: guest

4. Visit the "Queues" tab and create a queue.

5. Publish messages to the queue via Python3
