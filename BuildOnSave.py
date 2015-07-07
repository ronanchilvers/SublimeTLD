import sublime, sublime_plugin, re

class BuildOnSave(sublime_plugin.EventListener):

	def on_post_save(self, view):
		global_settings = sublime.load_settings(__name__ + '.sublime-settings')
		should_build    = view.settings().get('build_on_save', global_settings.get('build_on_save', True))
		build_filter    = view.settings().get('build_on_save_filter', '.*')

		if should_build:
			# print build_filter
			should_build = re.search(build_filter, view.file_name())

		if not should_build:
			# print "Not building"
			return

		# print "Building"
		view.window().run_command('build')
