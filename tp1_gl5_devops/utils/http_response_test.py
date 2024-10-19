from tp1_gl5_devops import createApp
from tp1_gl5_devops.utils.http_response import error_response, valid_response


class TestHttpResponseHelper:
    app = createApp()

    def test_error(self) -> None:
        with self.app.app_context():
            assert error_response('error', 400)

    def test_valid(self) -> None:
        with self.app.app_context():
            assert valid_response(['data'], 400)
