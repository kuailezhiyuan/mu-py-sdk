from mu.client import Client


def test_client():
    url = 'http://sp3.dev'
    client = Client(url)
    print(client.get_url())


if __name__ == '__main__':
    test_client()
