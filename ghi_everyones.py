import sublime, sublime_plugin
from github import *

class GhiEveryonesCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    # todo