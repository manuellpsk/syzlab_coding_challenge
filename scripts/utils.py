from core.models import User
import json
import os
from django.conf import settings
from tqdm.auto import tqdm


def populate_users():
    # Load json from fixtures/users.json
    fixture_path = os.path.join(settings.BASE_DIR, 'fixtures', 'users.json')
    with open(fixture_path, 'r') as _file:
        users_data = json.load(_file)
        for user_data in tqdm(users_data, desc="Populating Users"):
            fields = user_data.get('fields')
            del fields['groups']
            del fields['user_permissions']
            User.objects.create(**user_data.get('fields'))
