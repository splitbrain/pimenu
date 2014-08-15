#!/usr/bin/python2
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from functools import partial
import os
import subprocess

from libavg import app, avg
import sys
from components.button import Button
from components.tab import Tab
from components.tabset import TabSet


class PiMenu(app.MainDiv):
    tabs = []
    busyNode = None
    executing = False

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

        # create tabs and buttons
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
            self.tabs[i].tab.setCallback(self.onExecute)
            if i == 0:
                self.tabs[i].activate()
            else:
                self.tabs[i].deactivate()
            i = + 1

        self.initBusyNode()

    def initBusyNode(self):
        self.busyNode = avg.DivNode(
            pos=(0, 0),
            size=(self.width, self.height),
            parent=self
        )

        avg.RectNode(
            pos=(0, 0),
            size=(self.width, self.height),
            fillcolor="FFFFFF",
            fillopacity=1,
            strokewidth=0,
            parent=self.busyNode
        )
        fs = 25
        avg.WordsNode(
            pos=(self.width / 2, self.height / 2 - fs / 2),
            fontsize=fs,
            text='Please wait...',
            alignment='center',
            width=self.width,
            height=self.height,
            font='Arial',
            color='333333',
            variant='bold',
            parent=self.busyNode
        )
        self.busyNode.active = False

    def onExecute(self, section, button):
        if self.executing:
            return

        print section, button
        self.executing = True
        self.busyNode.active = True

        player = avg.Player.get()
        player.setTimeout(10, partial(self.doExecute, section, button)) # use timeout to leave time for rendering

    def doExecute(self, section, button):
        subprocess.call([os.path.dirname(os.path.realpath(sys.argv[0])) + '/pimenu.sh', section, button],
                        shell=True)
        self.busyNode.active = False
        self.executing = False

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

