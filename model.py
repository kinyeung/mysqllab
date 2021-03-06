from sqlalchemy import Column, Integer, String, Text, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostsRecord(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True, name="Id")
    post_type_id = Column(SmallInteger, name="PostTypeId")
    accepted_answer_id = Column(Integer, name="AcceptedAnswerId")
    parent_id = Column(Integer, name="ParentId")
    score = Column(Integer, name="Score")
    view_count = Column(Integer, name="ViewCount")
    body = Column(Text(), name="Body")
    owner_user_id = Column(Integer, name="OwnerUserId")
    owner_display_name = Column(String(256), name="OwnerDisplayName")
    last_editor_user_id = Column(Integer, name="LastEditorUserId")
    last_edit_date = Column(DateTime(), name="LastEditDate")
    last_activity_date = Column(DateTime(), name="LastActivityDate")
    title = Column(String(256), name="Title")
    tags = Column(String(256), name="Tags")
    answer_count = Column(Integer, name="AnswerCount")
    comment_count = Column(Integer, name="CommentCount")
    favorite_count = Column(Integer, name="FavoriteCount")
    creation_date = Column(DateTime(), name="CreationDate")

    __table_args__ = ({
        "mysql_charset": "utf8",
    })

    def __init__(self):
        pass

    def make_copy(self):
        post = PostsRecord()

        post.id = self.id

        post.post_type_id = self.post_type_id

        post.accepted_answer_id = self.accepted_answer_id

        post.parent_id = self.parent_id

        post.score = self.score

        post.view_count = self.view_count

        post.body = self.body

        post.owner_user_id = self.owner_user_id

        post.owner_display_name = self.owner_display_name

        post.last_editor_user_id = self.last_editor_user_id

        post.last_edit_date = self.last_edit_date

        post.last_activity_date = self.last_activity_date

        post.title = self.title

        post.tags = self.tags

        post.answer_count = self.answer_count

        post.comment_count = self.comment_count

        post.favorite_count = self.favorite_count

        post.creation_date = self.creation_date

        return post

    def __repr__(self):
        return '<POSTS: id=%r score=%r title=%r tags=%r>' % (self.id, self.score, self.title, self.tags)

    @staticmethod
    def delete_all(session):
        session.query(PostsRecord).delete()
        session.commit()
