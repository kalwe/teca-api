import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class ExternalIntegrationService:
    """
    Handles integration with external platforms.
    """
    def __init__(self, base_url: str, timeout: int = 5):
        self.base_url = base_url
        self.session = self._create_session(timeout)

    def _create_session(self, timeout: int):
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        session.timeout = timeout
        return session

    def fetch_data(self, endpoint: str, params: dict = None) -> dict:
        response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
