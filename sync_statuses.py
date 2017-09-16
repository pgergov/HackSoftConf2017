import time
import requests


def get_status(url, session):
    response = session.get(url)

    return response.status_code


def get_statuses(urls):
    result = {}
    session = requests.Session()
    
    for url in urls:
        status = get_status(url, session)

        if not status in result:
            result[status] = 0
        result[status] += 1

    return result


def main():
    with open ('hack-sites.txt', 'r') as data:
        sites = data.read().splitlines()

    start = time.time()
    statuses = get_statuses(sites)
    end = time.time()

    print(statuses)
    print(end - start)


if __name__ == "__main__":
    main()
