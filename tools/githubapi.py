import requests

class GitHubReleases(object):
    '''
    class takes "owner" of the repository "repo" and current version "vers"

    To use it with cx_Freeze specify verify='cacert.pem' on requests.get()
    and on build_exe: include_files: [(requests.certs.where(), 'cacert.pem'), ...]
    with "import requests.certs".
    '''

    def __init__(self, owner='', repo='', vers=''):
        """
        Note: GET method for GitHub API v3 couldn`t be requests.get(url, params)
        instead of that use requests.get(url.format(owner, repo)).
        """

        def hasError(e):
            self.hasRequestsError = True
            print('Got Exception "{e}"'.format((e)))

        self.owner = owner
        self.repo = repo
        self.vers = vers

        self.hasRequestsError = False

        try:
            r = requests.get(
                'https://api.github.com/repos/{owner}/{repo}/releases'.format(
                    owner=self.owner,
                    repo=self.repo
                ),
                verify='cacert.pem'
            )
            print('releases:\n', r.json())

            if r.status_code == requests.codes.ok:
                self.releases = [
                    {
                        'tag_name': rel.get('tag_name'),
                        'browser_download_url': rel.get('assets')[0].get('browser_download_url'),
                        'html_url': rel.get('html_url'),
                        'prerelease': rel.get('prerelease')
                    } for rel in r.json()
                ]

            elif len(self.releases) == 0:
                self.hasRequestsError = True

            else:
                self.hasRequestsError = True

        except requests.exceptions.RequestException as e:
            hasError(e)

        try:
            r = requests.get(
                    'https://api.github.com/repos/{owner}/{repo}/releases/latest'.format(
                        owner=self.owner,
                        repo=self.repo
                    ),
                    verify='cacert.pem'
                )
            print('lastest release:\n', r)

            if r.status_code == requests.codes.ok:
                latest = r.json()

                self.latest = {
                    'tag_name': latest.get('tag_name'),
                    'browser_download_url': latest.get('assets')[0].get('browser_download_url'),
                    'html_url': latest.get('html_url'),
                    'prerelease': latest.get('prerelease')
                }

            else:
                self.latest = {
                    'tag_name': '',
                    'browser_download_url': '',
                    'html_url': '',
                    'prerelease': ''
                }
                self.hasRequestsError = True

        except Exception as e:
            hasError(e)

    def downloadStableRelease(self):
        '''
        return a tuple with the following fields:
        - noError:bool during requests.get()
        - tag_name:string available stable release
        - prerelease:bool pre- or release version
        - browser_download_url:string url to download new release.
        '''
        bad = (False, '', '', '')

        if self.hasRequestsError:
            return bad

        else:

            toint = lambda s: int(''.join(s.split('.')))

            old, new = toint(self.vers), toint(self.latest.get('tag_name'))

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
