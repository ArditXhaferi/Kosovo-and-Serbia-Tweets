from db import create_or_update_db
from tweets import get_tweets

create_or_update_db(
    get_tweets()
)