import sublime, sublime_plugin
from github import *

class GhiSearchCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    # todo