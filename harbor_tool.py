#!/usr/bin/env python

import requests
import json

from datetime import datetime, timedelta


class Harbor:

    def __init__(self):
        self.headers = {'accept': 'text/plain', 'content-type': 'application/json'}

    @staticmethod
    def project_list(url, user, password):
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
        TITLE = "{:<26}{:<10}{:<14}{:<26}{:<26}".format('Project', 'Id', 'Repo Count', 'Create Time', 'Update Time')
        project_data = requests.get(
            "https://{}/api/projects".format(url),
            headers={'accept': 'text/plain', 'content-type': 'application/json'},
            auth=(user, password)
            )
        project_data.raise_for_status()
        project_data = json.loads(project_data.text)

        print(TITLE)
        for i in project_data:
            project_name = i.get('name')
            project_id = i.get('project_id')
            project_repo = i.get('repo_count')
            project_create_time = datetime.strptime(i.get('creation_time'), UTC_FORMAT) + timedelta(hours=8)
            project_update_time = datetime.strptime(i.get('update_time'), UTC_FORMAT) + timedelta(hours=8)
            print("{:<26}{:<10}{:<14}{:<26}{:<26}"
                  .format(project_name, project_id, project_repo, str(project_create_time), str(project_update_time)))

    @staticmethod
    def image_list(url, user, password, repo):
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        TITLE = "{:<15}{:<30}".format('Tags', 'Push Time')
        repo_data = requests.get(
            'https://{}/api/repositories/{}/tags'.format(url, repo),
            headers={'accept': 'text/plain', 'content-type': 'application/json'},
            auth=(user, password)
        )
        repo_data = json.loads(repo_data.text)
        repo_data.sort(key=lambda k: (k.get('push_time', 0)), reverse=True)

        print(TITLE)
        for i in repo_data:
            image_name = i.get('name')
            image_push_time = datetime.strptime(i.get('push_time'), UTC_FORMAT) + timedelta(hours=8)
            print("{:<15}{:<30}"
                  .format(image_name, str(image_push_time)))

    @staticmethod
    def image_retag(url, user, password, src, dst):
        dst_repo, dst_tag = dst.split(':')
        data = {"override": True, "src_image": src, "tag": dst_tag}
        data_json = json.dumps(data)
        r_post = requests.post(
            'https://{}/api/repositories/{}/tags'.format(url, dst_repo),
            headers={'accept': 'text/plain', 'content-type': 'application/json'},
            data=data_json,
            auth=(user, password))
        return r_post.status_code
