# SQLite-Celery-Concurrency
Main objective for this mini project is to test if SQLite can handle concurrency read performed by [Celery](https://docs.celeryproject.org/en/stable/index.html).
<br><br>

<h2>⚙️ Setting Up</h2>
In order to run the program in this repository, we must install stuff first.
<br><br>
<h3>1. Install Celery</h3>
➔ It’s a task queue with focus on real-time processing, while also supporting task scheduling.
<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;`pip install requirements.txt` or `pip install celery`<br><br>

<h3>2. Install RabbitMQ as a broker</h3>
➔ Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.<br>
➔ Celery requires a message transport to send and receive messages.
<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;`brew install rabbitmq`
<br>
&nbsp;&nbsp;&nbsp;&nbsp;(If you are using other than MacOS, look into this [guide](https://docs.celeryproject.org/en/stable/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq).)
<br><br>

<h3>3. Run Celery and RabbitMQ</h3>
Prior to running the actual program, we need to have Celery and RabbitMQ both running.
<br><br>
➔ Run RabbitMQ
<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;`sudo rabbitmq-server` or `sudo rabbitmq-server -detached`
<br>
&nbsp;&nbsp;&nbsp;&nbsp;(For more information, visit this [documentation](https://docs.celeryproject.org/en/stable/getting-started/brokers/rabbitmq.html#starting-stopping-the-rabbitmq-server))
<br><br>
➔ Start Workers
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;`celery -A tasks worker -c 3 -l INFO`
<br>
&nbsp;&nbsp;&nbsp;&nbsp;(You can omit `-c 3`. To learn more about basic configuration, visit [here](https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#starting-the-worker))
<br><br>

<h2>💻 Running the Program</h2>
With everything up and running, go ahead and run the following command :
<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;`python test_celery.py`
<br><br>
You should expect such result :
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;`Parallele example result :
[0, 2, 8, 18, 32, 50, 72, 98, 128, 162]`
