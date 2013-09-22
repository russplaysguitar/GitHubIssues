# using http://developer.github.com/v3/issues/#list-issues-for-a-repository
# passes current github user as "assignee" url parameter ( ?assignee=github_username )

import sublime, sublime_plugin
import httplib, json
from github import *


class GhiAssignedToYouCommand(GithubWindowCommand):
    @with_repo
    def run(self, repo):
        # get "user/repo"
        user_repo_path = repo.repository_path.replace("github.com/", "")

        #get current user ($ git config --get github.user)
        user = repo.git("config --get github.user")

        # make the http request
        try:
            conn = httplib.HTTPSConnection("api.github.com")
            url = "/repos/"+user_repo_path+"/issues?assignee="+user
            conn.request("GET", url)
            response = conn.getresponse()
            data = response.read()
        finally:
            conn.close()
        
        # parse the response data as json
        parsed_data = json.loads(data)

        if(len(parsed_data) == 0):
            print "No issues for: "+url
            return

        # get the list of github issues as iss#: title [label] #comments @
        list_of_titles = map(lambda issue: 
            str(issue["number"]) + ": " + issue["title"] + 
                reduce(lambda m, label:
                    m + " [" + label["name"] + "]",
                    issue["labels"], ""
                ) + (" (" + str(issue["comments"]) + ")" if issue["comments"] > 0 else "") +
                (" @" if issue["assignee"] else ""), 
            parsed_data)
        
        window = self.window
        # view = window.active_view()
        print url
        print list_of_titles
        window.show_quick_panel(list_of_titles, -1)
