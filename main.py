import os
from datetime import datetime
from typing import Optional

import git
from tabulate import tabulate

time_format = '%d.%m.%Y %H:%M:%S'


def get_current_commit_time(repo: git.Repo) -> str:
    current_commit_hash = repo.head.object.hexsha
    current_commit_time = repo.git.show('-s', '--format=%ci', current_commit_hash)
    return datetime.strptime(current_commit_time, '%Y-%m-%d %H:%M:%S %z').strftime(time_format)


def get_latest_commit_time(repo: git.Repo, branch: str) -> Optional[str]:
    commits = list(repo.iter_commits(branch, max_count=1))
    if commits:
        commit = commits[0]
        return commit.committed_datetime.strftime(time_format)
    else:
        return None


def main():

  

    
    project_folder = os.path.dirname(os.path.abspath(__file__))

    repo = git.Repo(project_folder)

    current_commit_time = get_current_commit_time(repo)
    latest_commit_time = get_latest_commit_time(repo, 'main')
    is_project_updated = current_commit_time == latest_commit_time

    now = datetime.now().strftime(time_format)

    data = tabulate([
        ['current_time', now],
        ['current_commit_time', current_commit_time],
        ['latest_commit_time', latest_commit_time],
        ['is_project_updated', is_project_updated]
    ])

    out_file_path = os.path.join(project_folder, 'test.txt')
    with open(out_file_path, mode='w', encoding='utf-8') as out_file:
        out_file.write(data)


if __name__ == '__main__':
    main()
