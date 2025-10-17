import pytest
from monApp import app, db
from monApp.models import User ,load_user

@pytest.fixture
def testuser():
    user = User("CDAL","AIGRE")
    assert user == load_user(user.get_id())