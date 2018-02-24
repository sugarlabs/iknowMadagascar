#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gettext import gettext as _

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton, StopButton

import pygame
import sugargame.canvas
import conozco


class Activity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1

        toolbox = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbox.toolbar.insert(activity_button, 0)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbox.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        stop_button.props.accelerator = _('<Ctrl>Q')
        toolbox.toolbar.insert(stop_button, -1)
        stop_button.show()

        toolbox.show()
        self.set_toolbar_box(toolbox)
        self.show_all()

        self.game = conozco.Conozco(self)
        self.game.canvas = sugargame.canvas.PygameCanvas(
            self, main=self.game.run, modules=[
                pygame.display, pygame.font, pygame.mixer])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()
