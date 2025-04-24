from urllib.parse import urlparse


def get_abbreviated_url(url: str) -> str:
    """
    Get an abbreviated version of the transmitted URL.
    """
    parsed_url = urlparse(url)
    abbreviated_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return abbreviated_url
