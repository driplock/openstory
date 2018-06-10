class Page:

  def __init__(self, page):
    self.set_page(page)
    self._char = {}
    self._narrator = ''
    self._options = {}
   

  def set_page(self, page):
    self._pnum = page

  def set_char_dialog(self, cdialog):
    self._char = cdialog

  def set_narrator_dialog(self, ndialog):
    self._char = ndialog

  def set_options(self, options):
    self._options = options

  def get_page(self):
    return self._pnum

  def get_char_dialog(self):
    return self._char

  def get_narrator_dialog(self):
    return self._narrator

  def get_options(self):
    return self._options
