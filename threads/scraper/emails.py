from concurrent.futures import Future
from typing import List

import requests
from concurrent.futures.thread import ThreadPoolExecutor


def get_unique_emails(person_name, https):
    unique_emails = []

    resopnse = requests.get(https)
    comments_json = resopnse.json()

    for comment in comments_json:
        email = comment['email']
        if email not in unique_emails:
            unique_emails.append(email)

    return [person_name, unique_emails]


if __name__ == '__main__':
    executor = ThreadPoolExecutor(8)
    jobs: List[Future] = []
    # jobs = []
    emails_per_job = {}

    for i in range(1, 11):
        job = executor.submit(get_unique_emails,
                              f'job{i}',
                              f'https://jsonplaceholder.typicode.com/posts/{i}/comments')
        jobs.append(job)

    for job in jobs:
        emails_per_job[job.result()[0]] = job.result()[1]

    for key, value in emails_per_job.items():
        print(f'Emails for {key}')
        print(value)
