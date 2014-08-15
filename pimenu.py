#!/usr/bin/python2
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import copy
import os

from libavg import app, avg
import sys
from components.button import Button
from components.tab import Tab
from components.tabset import TabSet


class PiMenu(app.MainDiv):
    tabs = []

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
        self.tabs = [TabSet] * len(Config.sections())
        for section in Config.sections():
            self.tabs[i] = TabSet()

            self.tabs[i].btn = Button(self, i * tabwidth, 0, tabwidth, 50)
            self.tabs[i].btn.setText(section)
            self.tabs[i].btn.name = section
            self.tabs[i].btn.tabSet = i
            self.tabs[i].btn.setCallback(self.onTabClick)

            self.tabs[i].tab = Tab(self, 0, 50, width, height - 50, section)
            self.tabs[i].tab.createButtons(Config.items(section))
            if i == 0:
                self.tabs[i].activate()
            else:
                self.tabs[i].deactivate()

            i = + 1

    def onTabClick(self, event, node):
        """
        @type event: libavg.avg.Event
        @type node: Button
        """
        for tab in self.tabs:
            tab.deactivate()

        self.tabs[node.tabSet].activate()


    def onExit(self):
        pass

    def onFrame(self):
        pass


app.App().run(PiMenu(), app_resolution='320x240')

