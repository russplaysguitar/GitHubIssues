# using: http://developer.github.com/v3/issues/#list-issues-for-a-repository

import sublime, sublime_plugin
import httplib
from github import *


class GhiEveryonesCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        # get "user/repo"
        user_repo_path = repo.repository_path.replace("github.com/", "")
        try:
            conn = httplib.HTTPSConnection("api.github.com")
            url = "/repos/"+user_repo_path+"/issues"
            conn.request("GET", url)
            response = conn.getresponse()
            data = response.read()
        finally:
            conn.close()

        try:
            view = self.window.active_view()
            edit = view.begin_edit()
            view.insert(edit, 0, url)
            view.insert(edit, 0, data)
        finally:
            view.end_edit(edit)
