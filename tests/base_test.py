from app.app import create_app
from flask_testing import TestCase

from app.config import TestConfig


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app(TestConfig)
        return app

    def init_data(self):
        # demo = User(
        #         name=u'demo',
        #         email=u'demo@example.com',
        #         password=u'123456')
        # db.session.add(demo)
        # db.session.commit()
        pass

    def setUp(self):
        """Reset all tables before testing."""
        # db.create_all()
        print("setUp()")
        self.init_data()
        pass


    def tearDown(self):
        """Clean db session and drop all tables."""
        # db.session.remove()
        # db.drop_all()
        print("testDown()")
        pass


    def login(self, username, password):
        data = {
            'login': username,
            'password': password,
        }
        response = self.client.post('/login', data=data, follow_redirects=True)
        assert "Logged in" in response.data
        return response


    def _logout(self):
        response = self.client.get('/logout')
        self.assertRedirects(response, location='/')


    def _test_get_request(self, endpoint, template=None):
        response = self.client.get(endpoint)
        self.assert_200(response)
        if template:
            self.assertTemplateUsed(name=template)
        return response
