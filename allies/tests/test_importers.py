import pytest

from allies.models import Ally, HistoricalAlly
from allies.importers import BaseAllyImporter

pytestmark = pytest.mark.django_db

ALLY_1 = {
            "user_id": 1589437401,
            "username": "Pssst",
            "id": 1589437401,
            "avatar_type": 1,
            "avatar_id": 138,
            "last_shard_transfer": None,
            "home_world_id": None,
            "group_tag": "RE",
            "group_id": 1768651528,
            "power": None,
            "troop_kills": None,
            "active": True,
            "owner": {
                "user_id": 682872509,
                "username": "Kirra",
                "id": 682872509,
                "avatar_type": 1,
                "avatar_id": 1990700059,
                "last_shard_transfer": None,
                "home_world_id": None,
                "group_tag": "KTN",
                "group_id": 1477147334,
                "power": None,
                "troop_kills": None,
                "active": True
            },
            "cost": 549157694,
            "previous_cost": 523007328,
            "biome1_attack_multiplier": 0,
            "biome2_attack_multiplier": 0,
            "biome3_attack_multiplier": 1414,
            "biome4_attack_multiplier": 1326,
            "biome5_attack_multiplier": 1690,
            "biome6_attack_multiplier": 0,
            "biome7_attack_multiplier": 0,
            "biome8_attack_multiplier": 0
}

job = BaseAllyImporter(token='test')

@pytest.fixture
def formatted_data():
    return job.format_allies([ALLY_1])[0]

def test_format_allies(formatted_data):
    """
    Test that the format_allies method only returns keys that are in the model
    """
    model_fields = [f.name for f in Ally._meta.get_fields()]
    for key in formatted_data.keys():
        assert key in model_fields

    assert 'id' not in formatted_data.keys()
    assert isinstance(formatted_data['owner'], Ally)

def test_update_or_create_ally_initial_load(formatted_data):
    """
    Test update_or_create_current_ally successfully creates a CurrentAlly object
    """
    user_id = formatted_data['user_id']
    job.update_or_create_allies([formatted_data])
    ally = Ally.objects.get(user_id=user_id)
    for k, v in formatted_data.items():
        assert getattr(ally, k) == v

def test_update_or_create_ally_new_data(formatted_data):
    """
    Test update_or_create actually updates the CurrentAlly Object
    """
    user_id = formatted_data['user_id']
    job.update_or_create_allies([formatted_data])
    new_owner = ALLY_1['owner']
    new_owner['user_id'] = 123456
    new_owner = job.process_owner(new_owner)
    update_data = {
        'biome3_attack_multiplier': 1500,
        'biome4_attack_multiplier': 1400,
        'biome5_attack_multiplier': 1700,
        'owner': new_owner
    }
    formatted_data.update(update_data)
    job.update_or_create_allies([formatted_data])
    ally = Ally.objects.get(user_id=user_id)
    for key, value in update_data.items():
        assert getattr(ally, key) == value
    # Should be 3 objects. The initial ally, and both owners
    assert Ally.objects.count() == 3

def test_create_historical_allies_no_change(formatted_data):
    """
    Test create_historical_allies does not duplicate records when data hasn't changed
    """
    job.create_historical_ally(formatted_data)
    job.create_historical_ally(formatted_data)
    assert HistoricalAlly.objects.count() == 1

def test_create_historical_allies_with_changes(formatted_data):
    """
    Test create_historical_allies creates two HistoricalAlly objects to capture data change
    """
    ally = job.create_historical_ally(formatted_data)
    assert ally.cost == ALLY_1['cost']
    formatted_data['cost'] = 434343432
    updated_ally = job.create_historical_ally(formatted_data)
    assert updated_ally.cost == 434343432
    assert HistoricalAlly.objects.count() == 2
