# -*- coding: utf-8 -*-

import requests
import os


def new_proxy(uname, target_url, url=None, token=None):
    """post new proxy rule.

    Parameters
    ----------
    uname : str
        User name.
    target_url : str
        Base url of user's notebook server, w/o username.
    url : str
        Base url of proxy server, by default read from `PROXY_BASE`.
    token : str
        String required to communicate with proxy server, by default
        read from `PROXY_TOKEN`.

    Returns
    -------
    ret : str
        Proxy URL of target url.
    """
    # create proxy rule for user/container
    # add proxy url into container as new col
    # update template with proxy url and hide notebook_url
    if url is None:
        if 'PROXY_BASE' in os.environ:
            url = os.environ['PROXY_BASE']
        else:
            return None

    if token is None:
        if 'PROXY_TOKEN' in os.environ:
            token = os.environ['PROXY_TOKEN']
        else:
            token = ''

    purl = url + '/{}/'.format(uname)
    r = requests.post(purl,
            json={
                'target': target_url,
            },
            headers={'Authorization': 'token {}'.format(token)},
        )
    if r.ok:
        return r.url
    else:
        return None
