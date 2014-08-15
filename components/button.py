from libavg.avg import LinearAnim
from libavg import avg


class Button(avg.DivNode):
    fontsize = 20
    _rectNode = None
    _textNode = None
    _callback = None

    def __init__(self, parent, x, y, w, h):
        super(Button, self).__init__(
            pos=(x, y),
            size=(w, h),
        )
        self.registerInstance(self, parent)

        self._rectNode = avg.RectNode(
            pos=(0, 0),
            size=(w, h),
            fillcolor="CCCCCC",
            fillopacity=1,
            strokewidth=0,
            parent=self
        )

        self.subscribe(self.CURSOR_UP, self._clicked)

    def setText(self, text):
        """
        Sets the text of the button

        @type text: str
        """
        if self._textNode:
            self._textNode.text = text
        else:
            self._textNode = avg.WordsNode(
                text=text,
                alignment='center',
                width=self.width,
                height=self.height,
                fontsize=self.fontsize,
                pos=(self.width / 2, self.height / 2 - self.fontsize / 2),
                font='Arial',
                color='333333',
                variant='bold',
                parent=self
            )

    def setColor(self, color):
        self._rectNode.fillcolor = color

    def setCallback(self, cb):
        self._callback = cb

    def _clicked(self, event):
        fadeout = LinearAnim(self._rectNode, 'fillopacity', 100, self._rectNode.fillopacity, 0.5)
        fadein  = LinearAnim(self._rectNode, 'fillopacity', 100, 0.5, 1)

        player = avg.Player.get()
        player.setTimeout(0, fadeout.start)
        player.setTimeout(100, fadein.start)

        if self._callback:
            self._callback(event, self)