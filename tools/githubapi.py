import socket

import requests
import requests.certs

"""
Check the lastest release of your project
on www.github.com using GitHub API v3
(https://developer.github.com/v3).

author: UlrichVonRekkenin
mail: ulrihlebedev on gmail.com
date: 25/07/2015
"""

VERIFY = 'cacert.pem'
REMOTE_SERVER = 'www.github.com'

dummy = {
    'tag_name': '',
    'browser_download_url': '',
    'html_url': '',
    'prerelease': ''
}

bad = (False, '', '', '')


def isConnected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
        return False


class GitHubReleases(object):
    '''
    class takes "owner" of the repository "repo" and current version "vers"

    To use it with cx_Freeze specify const VERIFY = 'cacert.pem' to pass  requests.get()
    and on build_exe: include_files: [(requests.certs.where(), 'cacert.pem'), ...]
    with "import requests.certs".
    '''

    def __init__(self, owner='', repo='', vers=''):
        """
        Note: GET method for GitHub API v3 couldn`t be requests.get(url, params)
        instead of that use requests.get(url.format(owner, repo)).
        """

        self.owner = owner
        self.repo = repo
        self.vers = vers
        self.connection = isConnected()
        self.releases = []
        self.latest = dummy

    def getReleases(self):

        if self.connection:

            print('connected to www.github.com...')
            self.hasRequestsError = False

            try:
                r = requests.get(
                    'https://api.github.com/repos/{owner}/{repo}/releases'.format(
                        owner=self.owner,
                        repo=self.repo
                    ),
                    verify=VERIFY
                )
                print('releases:\n', r.json())

                if r.status_code == requests.codes.ok:
                    self.releases = [
                        {
                            'tag_name': rel.get('tag_name'),
                            'browser_download_url':
                                rel.get('assets')[0].get('browser_download_url'),
                            'html_url': rel.get('html_url'),
                            'prerelease': rel.get('prerelease')
                        } for rel in r.json()
                    ]

                elif len(self.releases) == 0:
                    self.hasRequestsError = True

                else:
                    self.hasRequestsError = True

            except Exception as e:
                self.hasRequestsError = True

    def getLatestRelease(self):
        if self.connection:
            try:
                r = requests.get(
                    'https://api.github.com/repos/{owner}/{repo}/releases/latest'.format(
                        owner=self.owner,
                        repo=self.repo
                    ),
                    verify=VERIFY
                )
                print('latest release:\n', r)

                if r.status_code == requests.codes.ok:
                    latest = r.json()

                    self.latest = {
                        'tag_name': latest.get('tag_name'),
                        'browser_download_url':
                            latest.get('assets')[0].get('browser_download_url'),
                        'html_url': latest.get('html_url'),
                        'prerelease': latest.get('prerelease')
                    }

                else:
                    self.hasRequestsError = True

            except Exception as e:
                self.hasRequestsError = True

        else:
            print('there is no internet connection...')
            self.hasRequestsError = True

    def downloadStableRelease(self):
        '''
        return a tuple with the following fields:
        :noError:bool during requests.get()
        :tag_name:string available stable release
        :prerelease:bool pre- or release version
        :browser_download_url:string url to download new release.
        '''

        self.getLatestRelease()

        if self.hasRequestsError:
            return bad

        else:

            old, new = int(self.vers.replace('.', '')), int(self.latest.get('tag_name').replace('.', ''))

            if old < new:
                print('No error, New stable version is available', self.latest.get('tag_name'))

                return (
                    True,
                    self.latest.get('tag_name'),
                    self.latest.get('prerelease'),
                    self.latest.get('browser_download_url')
                )

            else:
                return bad
