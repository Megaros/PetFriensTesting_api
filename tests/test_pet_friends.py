from api import PetFrands
from sittings import valid_email, valid_password

pf = PetFrands()

def test_get_api_key_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter = ''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200, 'Авторизация не прошла'
    assert len(result['pets']) > 0, 'Список животных пуст'
    print('Всего животных', len(result['pets']), 'шт')
def test_get_my_pets_with_valid_key(filter ='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200, 'Авторизация не прошла'
    assert len(result['pets']) > 0, 'Список животных пуст'
    print('Моих животных',len(result['pets']), 'шт')
