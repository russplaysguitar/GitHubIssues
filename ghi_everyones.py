# using http://developer.github.com/v3/issues/#list-issues-for-a-repository

import sublime, sublime_plugin
import httplib, json
from ghi import *
from github import *


class GhiEveryonesCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        # get "user/repo"
        user_repo_path = repo.repository_path.replace("github.com/", "")

        # make the http request
        try:
            conn = httplib.HTTPSConnection("api.github.com")
            url = "/repos/"+user_repo_path+"/issues"
            conn.request("GET", url)
            response = conn.getresponse()
            data = response.read()
        finally:
            conn.close()
        
        # parse the response data as json
        issues = json.loads(data)

        if(len(issues) == 0):
            print "No issues for: "+url
            return

        print url
        # print issues

        # get the list of github issues as iss#: title [label] #comments @
        list_of_titles = format_issues_list(issues)
        
        window = self.window
        window.show_quick_panel(list_of_titles, open_issue)
