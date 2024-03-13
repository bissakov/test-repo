from datetime import datetime

import git
from tabulate import tabulate

time_format = '%d.%m.%Y %H:%M:%S'


def get_latest_commit_time(repo_path) -> datetime or None:
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits('main', max_count=1))
    if commits:
        commit = commits[0]
        return commit.committed_datetime.strftime(time_format)
    else:
        return None


def main():
    latest_commit_time = get_latest_commit_time(r'D:\Work\test-repo')
    now = datetime.now().strftime(time_format)

    with open(r'D:\Work\test-repo\test.txt', 'w') as f:
        f.write(tabulate([['current_time', now], ['latest_commit_time', latest_commit_time]]))


if __name__ == '__main__':
    main()
