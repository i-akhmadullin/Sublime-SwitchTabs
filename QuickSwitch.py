# coding: utf-8

import sublime_plugin


class QuickSwitchCommand(sublime_plugin.WindowCommand):
    def run(self, group, index):
        self.window.run_command("focus_group", {"group": group - 1})
        self.window.run_command("select_by_index", {"index": index - 1})
