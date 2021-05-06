from dataclasses import dataclass

import faker

fake = faker.Faker()


@dataclass
class Topic:
    title: str = None
    text: str = None
    id: int = None


class Builder:

    @staticmethod
    def create_topic(title=None, text=None):
        if title is None:
            title = fake.lexify(text='?? ?? ??? ??????')

        if text is None:
            text = fake.bothify(text='?????  ##### ?#?#?#?  #? # ?# ?# ? ? #? #? ?# ??#?')

        return Topic(title=title, text=text)