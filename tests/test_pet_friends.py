from api import PetFrands
from sittings import valid_email, valid_password

pf = PetFrands()

def test_get_api_key_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
