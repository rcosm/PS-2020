from db.database_engine import DatabaseEngine as db
from db.issue import Issue
from db.screenshot import Screenshot
from db.user import User
from db.product import Product
from db.tag import Tag
from db.issue_tag import IssueTag


class Bug:
    def __init__(self):
        self.__product = None
        self.__description = None
        self.__reporter = None
        self.__assigned_user = None
        self.__tag = None
        self.__screenshot = None

    def find_bug_by_id(self, id):
        session = db.create_session()
        i = session.query(Issue).filter(Issue.id == id).first()
        self.__product = session.query(Product).filter(Product.id == i.product_id).first().name
        self.__reporter = session.query(User).filter(User.id == i.reporter_id).first().name
        self.__description = i.description
        if i.assigned_user_id is None:
            self.__assigned_user = None
        else:
            self.__assigned_user = session.query(User).filter(User.id == i.assigned_user_id).first().name

    def set_product(self, product_name):
        self.__product = product_name

    def set_description(self, description):
        self.__description = description

    def set_reporter(self, reporter):
        self.__reporter = reporter

    def set_assigned_user(self, assigned_user):
        self.__assigned_user = assigned_user

    def set_tag(self, tag):
        self.__tag = tag
    
    def set_screenshot(self, screenshot):
        self.__screenshot = screenshot

    def add(self):
        session = db.create_session()
        i = self.__create_bug(session)
        session.add(i)
        if self.__screenshot is not None:
            s = Screenshot(path_to_screenshot=self.__screenshot)
            s.issue_id = i.id
            session.add(s)
        if self.__tag is not None:
            t = session.query(Tag).filter(Tag.name == self.__tag).first()
            # it = IssueTag(issue_id=i.id, tag_id=t.id)
            # session.add(it)
        session.commit()

    def __create_bug(self, session):
        u = session.query(User).filter(User.name == self.__reporter).first()
        p = session.query(Product).filter(Product.name == self.__product).first()
        a = None
        if self.__assigned_user is not None:
            a = session.query(User).filter(User.name == self.__assigned_user).first()
        i = Issue(description=self.__description, reporter_id=u.id, product_id=p.id)
        if a is not None:
            i.assigned_user_id = a.id
        return i

    def print_current_bug(self):
        print("description: %s" % self.__description)
        print("product: %s" % self.__product)
        print("reporter: %s" % self.__reporter)
        print("assigned to: %s" % self.__assigned_user)
        print("tag: %s" % self.__tag)
        print("screenshot path: %s" % self.__screenshot)


if __name__ == "__main__":
    b = Bug()
    b.find_bug_by_id(1)
    b.print_current_bug()
    b.set_description("new test bug")
    b.set_assigned_user("Rares Cosma")
    b.set_product("Money Tracker")
    b.set_reporter("Vasile Cosma")
    b.set_tag("exploratory")
    b.add()
    bug = Bug()
    bug.find_bug_by_id(2)
    bug.print_current_bug()
