import pytest
from APIteatingFramework.apiframe import Methods, CustomLogging, ApiTests
import concurrent.futures


@pytest.fixture
def methods():
    api_client = Methods("path/to/api/config.json", CustomLogging(__file__))
    return api_client


@pytest.mark.smoke
def test_api_access(methods):
    request = methods.get_record(6914020)
    test = ApiTests(request)
    response = test.status_code(200)
    assert response == 0
    response = test.status_code_text("OK")
    assert response == 0


@pytest.mark.stress
def send_requests(methods):
    for _ in range(10):  # Adjust the number of requests as needed
        request = methods.get_records()
        test = ApiTests(request)
        response = test.status_code(200)
        assert response == 0
        response = test.status_code_text("OK")
        assert response == 0


@pytest.mark.stress
def test_stress_testing():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_requests) for _ in range(10)]  # Adjust the number of threads as needed
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Ensure all requests complete without error
