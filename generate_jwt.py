#!/usr/bin/env python3
import jwt
import time
import sys


def generate_jwt():

    # Get PEM file path
    if len(sys.argv) > 1:
        pem = "/home/edgar/Desktop/Projects/Python_projects/GitHub_API/github/jwt/apptestcase.2023-10-13.private-key.pem"
    else:
        pem = input("Enter path of private PEM file: ")

    # Get the App ID
    if len(sys.argv) > 2:
        app_id = sys.argv[2]
    else:
        app_id = input("Enter your APP ID: ")

    # Open PEM
    with open(pem, 'rb') as pem_file:
        signing_key = jwt.jwk_from_pem(pem_file.read())

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time (10 minutes maximum)
        'exp': int(time.time()) + 600,
        # GitHub App's identifier
        'iss': '407750'

    }

    # Create JWT
    jwt_instance = jwt.JWT()
    encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')

    return encoded_jwt
