#!/usr/bin/env python

import urllib2

class Sourcer(object):
  """A general class that is responsible for retrieving data

  Args:
    data_source: URL that's used to retrieve data

    custom_properties: A map that's used to help the Sourcer object retrieve data

  Raises:
    NotImplementedError: Raised if load_data method is not implemented
  """
  def __init__(self, data_source, custom_properties=None):
      self.source = data_source
      self.custom_properties = {}
      if custom_properties is not None:
        self.custom_properties = custom_properties

  def get_source(self):
    return self.source

  def get_custom_properties(self):
    return self.custom_properties

  def load_data(self):
    raise NotImplementedError("Should have implemented this")

# Hardcoded api client
class BibleSourcer(object):
  """A class dedicated to retrieving Bible data. Right now, this class uses the
  NET Bible Web Service API. Details can be found here:
  http://labs.bible.org/api_web_service. Will refactor if there's a better api.
  """
  url = 'http://labs.bible.org/api/?'
  format_properties = '&type=json&formatting=plain'

  @staticmethod
  def load_verse(book, chapter, verse):
    chptr, vrs = str(chapter), str(verse)
    req = ''.join([BibleSourcer.url, 'passage=', book, '%20', chptr, ':', vrs,
      BibleSourcer.format_properties])
    return urllib2.urlopen(req).read()

  @staticmethod
  def load_verses(book, chapter, from_verse, to_verse):
    chptr, from_vrs, to_vrs = str(chapter), str(from_verse), str(to_verse)
    verse_range = ''.join([from_vrs,'-',to_vrs])
    req = ''.join([BibleSourcer.url, 'passage=', book, '%20', chptr, ':',
      verse_range, BibleSourcer.format_properties])
    return urllib2.urlopen(req).read()

# Helper method
def url_fix(s, charset='utf-8'):
    """Sometimes you get an URL by a user that just isn't a real
    URL because it contains unsafe characters like ' ' and so on.  This
    function can fix some of the problems in a similar way browsers
    handle data entered by the user.

    :param charset: The target charset for the URL if the url was
                    given as unicode string.
    """
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))

