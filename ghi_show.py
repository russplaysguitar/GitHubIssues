import sublime, sublime_plugin
from github import *

class GhiShowCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    # todo