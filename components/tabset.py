class TabSet(object):

    btn = None
    tab = None

    def activate(self):
        if self.btn:
            self.btn.setColor('777777')
        if self.tab:
            self.tab.active = True

    def deactivate(self):
        if self.btn:
            self.btn.setColor('CCCCCC')
        if self.tab:
            self.tab.active = False

