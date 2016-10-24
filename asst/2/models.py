import datetime


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = datetime.date(year, month, day)

        # list of contributors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):

    def __init__(self, year, month, day, headline, content, contributors):
        super(Article, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self):
        print(headline + '\n\n' + content)


# TODO: Define a Picture class that extends the Content class
class Picture(Content):

    def  __init__(self, year, month, day, title, caption, path, contributors):
        super(Picture, self).__init__(year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        from PIL import Image
        im = Image.open(path)
        im.show()
        print(title + '\n' + caption)

