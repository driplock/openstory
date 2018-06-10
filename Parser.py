from collections import OrderedDict

class StoryParser:

  def __init__(self, story):
    self._story = story
    self._current_page = 0
    self._pageinfo = {}
  
  def parse_story(self, story=None):
    if story is None:
      story = self.get_raw_story()

    with open(story) as content: 
      self.set_page_info(content) 
  
  def set_page_info(self,contents): 
    for line in contents.readlines():
      self.build_page_object(line)
        
  def build_page_object(self,line):
    if 'Page' in line:
      self.add_page_object(line)
    else:
      self.add_page_info(line)

  def add_page_object(self,line):
    page_num = line.split(":")[1].strip()
    self.set_current_page(page_num)
    self._pageinfo.update({page_num: OrderedDict()})

  def add_page_info(self,line):
    if len(line) > 1:
      keyval = line.split(":",1)
      if len(keyval) > 1:
        self._pageinfo[self.get_current_page()].update({keyval[0].strip():keyval[1].strip()})
      else:
        last_key = self._pageinfo[self.get_current_page()].keys()[-1]
        last_val = self._pageinfo[self.get_current_page()][last_key]
        self._pageinfo[self.get_current_page()].update({last_key:last_val + " " + keyval[0]})
   
  def get_page_info(self):
    return self._pageinfo 

  def get_raw_story(self):
    return self._story

  def set_current_page(self,cpage):
    self._current_page = cpage

  def get_current_page(self):
    return self._current_page
