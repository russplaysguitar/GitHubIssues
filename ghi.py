def format_issues_list(issues):
    return map(lambda issue: 
        str(issue["number"]) + ": " + issue["title"] + 
            reduce(lambda memo, label:
                memo + " [" + label["name"] + "]",
                issue["labels"], ""
            ) + (" (" + str(issue["comments"]) + ")" if issue["comments"] > 0 else "") +
            (" @" if issue["assignee"] else ""), 
        issues)

def open_issue(issue_list_number):
    print issue_list_number
    return #todo