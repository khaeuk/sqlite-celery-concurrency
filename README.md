# SQLite-Celery-Concurrency
[![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)
![Celery](https://img.shields.io/badge/-Celery-eee?style=flat&logo=celery&logoColor=678d2c)
![RabbitMQ](https://img.shields.io/badge/-RabbitMQ-eee?style=flat&logo=rabbitmq&logoColor=f76401)

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

&nbsp;&nbsp;&nbsp;&nbsp;`python test_concurency_read.py`
<br><br>
You should expect such result :
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;`Single task example result :
[(1, 5.1, 3.5, 1.4, 0.2, 'Iris-setosa'), (2, 4.9, 3, 1.4, 0.2, 'Iris-setosa'), (3, 4.7, 3.2, 1.3, 0.2, 'Iris-setosa'), (4, 4.6, 3.1, 1.5, 0.2, 'Iris-setosa'), (5, 5, 3.6, 1.4, 0.2, 'Iris-setosa')]
Multiple parallel tasks example result :
[[[1, 5.1, 3.5, 1.4, 0.2, 'Iris-setosa'], [2, 4.9, 3, 1.4, 0.2, 'Iris-setosa'], [3, 4.7, 3.2, 1.3, 0.2, 'Iris-setosa'], [4, 4.6, 3.1, 1.5, 0.2, 'Iris-setosa'], [5, 5, 3.6, 1.4, 0.2, 'Iris-setosa']], [[51, 7, 3.2, 4.7, 1.4, 'Iris-versicolor'], [52, 6.4, 3.2, 4.5, 1.5, 'Iris-versicolor'], [53, 6.9, 3.1, 4.9, 1.5, 'Iris-versicolor'], [54, 5.5, 2.3, 4, 1.3, 'Iris-versicolor'], [55, 6.5, 2.8, 4.6, 1.5, 'Iris-versicolor']], [[101, 6.3, 3.3, 6, 2.5, 'Iris-virginica'], [102, 5.8, 2.7, 5.1, 1.9, 'Iris-virginica'], [103, 7.1, 3, 5.9, 2.1, 'Iris-virginica'], [104, 6.3, 2.9, 5.6, 1.8, 'Iris-virginica'], [105, 6.5, 3, 5.8, 2.2, 'Iris-virginica']]]`

