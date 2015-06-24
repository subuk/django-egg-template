from {{ project_name }}.tests.base import BaseTestCase


class IndexTestCase(BaseTestCase):

    def test_get_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
