import factory

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: "John%s" % n)
    last_name = factory.Sequence(lambda n: "Doe%s" % n)
    email = factory.LazyAttribute(lambda o: "%s@example.com" % o.first_name.lower())
    password = factory.LazyFunction(lambda: make_password("password"))

    class Meta:
        model = User
