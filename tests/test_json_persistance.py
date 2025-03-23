
import pytest

from json_persistance import JsonPersistence


def test_save_rejects_string():
    jp = JsonPersistence('fake.json')
    with pytest.raises(ValueError):
        jp.save("rozwal ostaecznie dzejsona bo sie odradza")



