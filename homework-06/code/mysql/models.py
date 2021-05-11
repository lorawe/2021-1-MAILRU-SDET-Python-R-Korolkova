from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CountRequest(Base):
    __tablename__ = 'count_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Count(" \
               f"id='{self.id}'," \
               f"count='{self.count}'" \
               f")>"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=True, primary_key=True)


class CountMethod(Base):
    __tablename__ = 'count_methods'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<CountMethod(" \
               f"id='{self.id}'," \
               f"method='{self.method}'," \
               f"count='{self.count}'" \
               f")>"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    method = Column(String(300), nullable=False)
    count = Column(Integer, nullable=False)


class TopRequest(Base):
    __tablename__ = 'top_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TopRequest(" \
               f"id='{self.id}'," \
               f"count='{self.count}'," \
               f"url='{self.url}'" \
               f")>"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    url = Column(String(300), nullable=False)


class BadRequest(Base):
    __tablename__ = 'bad_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<BadRequest(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"status='{self.status}', " \
               f"surname='{self.weight}', " \
               f"start_teaching='{self.ip}'" \
               f")>"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    status = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)


class ServerErrorRequest(Base):
    __tablename__ = 'server_err_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<ServerErrorRequest(" \
               f"id='{self.id}'," \
               f"count='{self.count}'," \
               f"ip='{self.ip}'" \
               f")>"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)
