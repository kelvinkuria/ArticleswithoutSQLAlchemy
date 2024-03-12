class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string between 5 and 50 characters.")
        self._title = title
        self._author = author
        self._magazine = magazine
        self._author._articles.append(self)
        self._magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of Author.")
        self._author._articles.remove(self)
        self._author = new_author
        new_author._articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        self._magazine._articles.remove(self)
        self._magazine = new_magazine
        new_magazine._articles.append(self)

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise ValueError("Cannot modify author name after instantiation.")
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name

    @property
    def articles(self):
        return list(self._articles)  # Access the articles list using self.articles

    def magazines(self):
        magazines = set()
        for article in self._articles:
            magazines.add(article.magazine)
        return list(magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        categories = set(article.magazine.category for article in self._articles)
        return list(categories)

class Magazine:
    _magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = new_category

    @property
    def articles(self):
        return list(self._articles)  # Access the articles list using self.articles

    def contributors(self):
        contributors = set()
        for article in self._articles:
            contributors.add(article.author)
        return list(contributors)

    def article_titles(self):
        if not self._articles:
            return None
        titles = [article.title for article in self._articles]
        return titles

    def contributing_authors(self):
        if not self._articles:
            return None
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        authors_with_more_than_two = [author for author, count in author_counts.items() if count > 2]
        return authors_with_more_than_two

    @classmethod
    def top_publisher(cls):
        if not cls._magazines:
            return None
        max_articles = max(len(magazine._articles) for magazine in cls._magazines)
        top_magazines = [magazine for magazine in cls._magazines if len(magazine._articles) == max_articles]
        return top_magazines[0]
