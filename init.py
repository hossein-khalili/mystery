from database import db_session
from database import init_db
from models import User

init_db()
u = User("farima", 1)
db_session.add(u)
db_session.commit()