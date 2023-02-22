import requests
from requests.adapters import HTTPAdapter, Retry

__version__ = "0.1.0"


class CNPJClient:

    BASE_URL = "https://api.cnpjs.dev"

    def __init__(self, base_url=None, max_retries=5, backoff_factor=0.2):
        self.base_url = base_url or self.BASE_URL
        self.session = requests.Session()
        retry = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504],
        )
        self.session.mount("https://api.cnpjs.dev", HTTPAdapter(max_retries=retry))
        self.session.headers.update({"User-Agent": f"cnpj-py/{__version__}"})

    def cnpj(self, cnpj: str):
        try:
            response = self.session.get(f"{self.base_url}/v1/{cnpj}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            raise CNPJError from exc


class CNPJError(RuntimeError):
    ...
