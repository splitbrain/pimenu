from libavg import avg
from components.button import Button


class Tab(avg.DivNode):
    name = None
    _callback = None

    def __init__(self, parent, x, y, w, h, name):
        super(Tab, self).__init__(
            pos=(x, y),
            size=(w, h),
        )
        self.registerInstance(self, parent)

        self.name = name

    def createButtons(self, opts):
        btnheight = (self.height - len(opts)) / len(opts)
        i = 0
        for (name, label) in opts:
            button = Button(self, 0, (i * (btnheight + 1)) + 1, self.width, btnheight)
            button.setText(label)
            button.name = name
            button.setCallback(self.onClick)
            i += 1

    def setCallback(self, callback):
        self._callback = callback

    def onClick(self, event, node):
        """
        @type event: libavg.avg.Event
        @type node: Button
        """
        if self._callback:
            self._callback(self.name, node.name)
