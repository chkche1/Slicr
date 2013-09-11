# Support enum class in python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

# Should write handler for each case in the future...
UNIT = enum('NONE', 'BOOK', 'CHAPTER', 'CUSTOM')


class Book(object):
  """Stores data that identifies a book.
  """
  def __init__(self, title, author, isbn=None, unit=UNIT.NONE):
    self.title = title
    self.author = author
    self.isbn = isbn
    if unit is UNIT.NONE or unit not in UNIT:
      raise ValueError("unit must be valid and defined for a book")

class BookMark(object):
  """Stores reading progress of an user

  """
  def __init__(self, user, book):
    # progress tracks high-level logical blocks
    # pos tracks progress at finer granularity (nth character)
    self._user = user
    self._progress = -1
    self._pos = 0
    if not isinstance(book, Book):
      raise ValueError("book must be an instance of Book")

  @property
  def user(self):
    return self._user

  @property
  def progress(self):
    return self._progress

  @property
  def pos(self):
    return self._pos

  @progress.setter
  def set_progress(self, progress):
    self._progress = progress

  @pos.setter
  def set_pos(self, pos):
    self._pos = pos


