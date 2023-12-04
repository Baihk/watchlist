import unittest
from app import app, db, Movie, User, forge, initdb


class WatchlistTestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        user = User(name='Test', username='test')
        user.set_password('123')
        movie = Movie(title='Test Movie Title', year='2019')
        db.session.add_all([user, movie])
        db.session.commit()

        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self):
        self.client.post('/login', data=dict(
            username='test',
            password='123'
        ), follow_redirects=True)

    def test_app_exist(self):
        self.assertIsNotNone(app)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])




if __name__ == '__main__':
    unittest.main()