from requests_html import HTMLSession
import certifi

BASE_URL = "https://hl7-definition.caristix.com/v2/"


def get_definition(segment_name, segment_field, version="2.3"):
    url = f"{BASE_URL}HL7v{version}/Fields/{segment_name}.{segment_field}"
    return url
    session = HTMLSession()
    r = session.get(url, cert=())
    return r.html.render()
