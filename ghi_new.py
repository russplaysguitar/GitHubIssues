import sublime, sublime_plugin
from github import *

class GhiNewCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    # todo