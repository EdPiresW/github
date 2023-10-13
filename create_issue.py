#!/usr/bin/env python3
# pylint: disable=line-too-long
"""
Get files names from the GitHub for a given organization
"""
import generate_jwt
import json
import netrc
import requests
import urllib3

#!/usr/bin/env python3
import jwt
import time
import sys


def generate_jwt():
    # Get PEM file path
    pem = "/home/edgar/Desktop/Projects/Python_projects/GitHub_API/github/jwt/apptestcase.2023-10-13.private-key.pem"

    with open(pem, "rb") as pem_file:
        signing_key = jwt.jwk_from_pem(pem_file.read())

    payload = {
        # Issued at time
        "iat": int(time.time()),
        # JWT expiration time (10 minutes maximum)
        "exp": int(time.time()) + 600,
        # GitHub App's identifier
        "iss": "407750",
    }

    # Create JWT
    jwt_instance = jwt.JWT()
    encoded_jwt = jwt_instance.encode(payload, signing_key, alg="RS256")

    return encoded_jwt


def create_issue():
    """
    create an issue,
    using the github REST API.
    """

    url = f"https://api.github.com/repos/EdPiresW/github/issues"

    headers_with_mytoken = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {my_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    headers_with_jwt = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {generate_jwt()}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    data_update = {
        "title": "Found a bug",
        "body": "I am having a problem with this.",
        "labels": ["bug"],
    }

    release_data = {
        "tag_name": "v1.0.0",
        "target_commitish": "master",
        "name": "v1.0.0",
        "body": "Description of the release",
        "draft": "false",
        "prerelease": "false",
        "generate_release_notes": "false",
    }

    data_update_json = json.dumps(data_update)

    app_installation = requests.get(
        url="https://api.github.com/app/installations", headers=headers_with_jwt
    )
    app_installation = app_installation.json()
    # print(app_installation)
    # print(app_installation[0]["html_url"])
    authenticate_2 = requests.post(
        url="https://api.github.com/app/installations/42850779/access_tokens",
        headers=headers_with_jwt,
    )
    token = authenticate_2.json()["token"]

    headers_info_my_token = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # response = requests.post(
    #     url="https://api.github.com/repos/EdPiresW/github/issues",
    #     headers=headers_info_my_token,
    #     data=data_update_json,
    # )

    response = requests.post(
        url="https://api.github.com/repos/EdPiresW/github/releases",
        headers=headers_with_mytoken,
        data=release_data,
    )

    response_json = response.json()

    print(response_json)


create_issue()
