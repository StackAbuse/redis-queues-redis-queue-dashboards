# To assign redis as backend to rq
from redis import Redis
# To initialize the queue object
from rq import Queue
# Functions from the __main__ module can't be processed by workers
# Hence, we have a separate python file containing the function
from test_job import i_am_a_job


# Create the queue object by passing in the redis object
q = Queue(connection=Redis())

# Run the job asynchronously
job = q.enqueue(i_am_a_job, 1)
# Return the function output
