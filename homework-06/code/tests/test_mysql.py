import pytest

from mysql.builder import MySQLBuilder
from mysql.models import BadRequest, ServerErrorRequest, CountMethod, CountRequest, TopRequest
import scripts.log_handler as scripts


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestMysql(MySQLBase):

    def prepare(self):
        self.count_requests = scripts.count_requests()
        self.count_methods = scripts.count_methods()
        self.top_requests = scripts.top10_requests()
        self.bad_requests = scripts.top5_heavy4XX()
        self.server_err_requests = scripts.top5_count5XX()

    def get_count_request(self):
        count_requests = self.mysql.session.query(CountRequest).all()
        print(count_requests)
        return count_requests

    def get_count_method(self):
        count_method = self.mysql.session.query(CountMethod).all()
        print(count_method)
        return count_method

    def get_top_request(self):
        top_requests = self.mysql.session.query(TopRequest).all()
        print(top_requests)
        return top_requests

    def get_bad_request(self):
        bad_requests = self.mysql.session.query(BadRequest).all()
        print(bad_requests)
        return bad_requests

    def get_server_err_request(self):
        server_err_requests = self.mysql.session.query(ServerErrorRequest).all()
        print(server_err_requests)
        return server_err_requests

    def test_count_request(self):
        self.mysql_builder.create_count_request(count=self.count_requests)
        count_request = self.get_count_request()
        assert len(count_request) == 1

    def test_count_method(self):
        for method in self.count_methods:
            self.count_method = self.mysql_builder.create_count_method(method=self.count_methods[method], count=method)

        count_request = self.get_count_method()
        assert len(count_request) == 5

    def test_top_request(self):
        for top in self.top_requests:
            self.count_method = self.mysql_builder.create_top_request(url=self.top_requests[top], count=top)

        count_request = self.get_top_request()
        assert len(count_request) == 10

    def test_bad_request(self):
        for bad in self.bad_requests:
            self.count_method = self.mysql_builder.create_bad_request(url=bad[0], status=bad[1], weight=bad[2],
                                                                      ip=bad[3])
        count_request = self.get_bad_request()
        assert len(count_request) == 5

    def test_server_err_request(self):
        for err in self.server_err_requests:
            self.count_method = self.mysql_builder.create_server_err_request(count=self.server_err_requests[err],
                                                                             ip=err)

        count_request = self.get_server_err_request()
        assert len(count_request) == 5
