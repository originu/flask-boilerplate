from tests.base_test import BaseTestCase


class TestServerResource(BaseTestCase):

    def test_get_version(self):
        response = self.client.get('/api/server/version')
        if response.status_code == 200:
            print(response.json)
            assert True
        else:
            print(response.data)
            assert False
        pass
