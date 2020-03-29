import json
from db.database_engine import DatabaseEngine as db
from db.user import User
from db.tag import Tag
from db.issue import Issue
from db.screenshot import Screenshot
from db.comment import Comment
from db.product import Product

def init_db():
    db.create_tables()

    session = db.create_session()
    with open('db_data.json') as f:
        data = json.load(f)
        for user in data['user']:
            u = User(username=user['username'], password=user['password'], name=user['name'])
            session.add(u)
        for tag in data['tag']:
            t = Tag(name=tag['name'])
            session.add(t)
        for product in data['product']:
            p = Product(name=product['name'])
            session.add(p)
    session.commit()

    i = Issue(description="Updater doesn't work on linux", reporter_id=1, product_id=1)
    session = db.create_session()
    session.add(i)
    session.commit()

    s = Screenshot(issue_id=1, path_to_screenshot=r'db_diagram.png')
    session = db.create_session()
    session.add(s)
    session.commit()

    c = Comment(issue_id=1, user_id=2, message="Are you sure? I ran it last week on a CentOS and it seemed to be working just fine")
    session = db.create_session()
    session.add(c)
    session.commit()


if __name__ == '__main__':
    init_db()
