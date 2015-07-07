import sublime, sublime_plugin, re

class FoldOnOpen(sublime_plugin.EventListener):
    def on_load(self, view):

        global_settings     = sublime.load_settings(__name__ + '.sublime-settings')
        should_run          = view.settings().get('fold_on_open', global_settings.get('fold_on_open', True))

        if should_run:
            run_filter  = view.settings().get('fold_on_open_filter', '.*')
            should_run  = re.search(run_filter, view.file_name())

        if not should_run:
            return

        fold_level          = view.settings().get('fold_on_open_level', 2)
        view.run_command("fold_by_level", {"level": fold_level})
