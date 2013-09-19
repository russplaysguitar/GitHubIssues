import sublime
import sublime_plugin
from github import *


class GhiAssignedToYouCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        one = 1
