#!/usr/bin/python2
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import os

from libavg import app, avg
import sys
from components.button import Button


class PiMenu(app.MainDiv):

    def onInit(self):
        (width, height) = app.instance._resolution

        # create white background
        avg.RectNode(
            pos=(0, 0),
            size=(width, height),
            fillcolor="FFFFFF",
            fillopacity=1,
            strokewidth=0,
            parent=self
        )

        # parse the config
        Config = SafeConfigParser()
        Config.read(os.path.dirname(os.path.realpath(sys.argv[0])) + '/pimenu.ini')

        # create buttons
        tabwidth = width / len(Config.sections())
        i = 0
        for section in Config.sections():
            button = Button(self, i, 0, tabwidth, 50)
            button.setText(section)
            button.name = section
            button.setCallback(self.onClick)
            i += tabwidth

    def onClick(self, event, node):
        """
        @type event: libavg.avg.Event
        """
        print node.name




    def onExit(self):
        pass

    def onFrame(self):
        pass


app.App().run(PiMenu(), app_resolution='320x240')