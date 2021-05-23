import pytest

from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_PYTHON')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()



def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_PYTHON')
        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_count_requests()
        mysql_client.create_count_methods()
        mysql_client.create_top_requests()
        mysql_client.create_bad_requests()
        mysql_client.create_server_err_requests()

        mysql_client.connection.close()
