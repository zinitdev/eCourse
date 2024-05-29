from app import ma, db
from .models import Category, Course, Tag, Lesson, User
from marshmallow import post_load, fields


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        fields = ['name']


class CourseSchema(ma.SQLAlchemyAutoSchema):
    category = ma.Function(lambda obj: obj.category.name)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'image',
                  'price', 'category', 'date_created']


class CourseDetailSchema(CourseSchema):
    tags = ma.List(ma.Nested(TagSchema))

    class Meta:
        model = CourseSchema.Meta.model
        fields = CourseSchema.Meta.fields + ['description', 'tags']


class LessonSchema(ma.SQLAlchemyAutoSchema):
    course = ma.Function(lambda obj: obj.course.subject)

    class Meta:
        model = Course
        fields = ['id', 'title', 'image', 'course', 'date_created']


class LessonDetailSchema(LessonSchema):
    tags = ma.List(ma.Nested(TagSchema))

    class Meta:
        model = LessonSchema.Meta.model
        fields = LessonSchema.Meta.fields + ['content', 'tags']


class UserSchema(ma.SQLAlchemyAutoSchema):
    password = fields.Str(load_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'username', 'password', 'avatar']

    @post_load
    def make_user(self, data, **kwargs):
        user = User(**data)
        user.set_password(data["password"])
        db.session.add_all(user)
        db.session.commit()
        return user