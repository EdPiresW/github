create a webhook

Need a payload url, we can create in https://smee.io/

Which events would you like to trigger this webhook?
    we need to selected what only what e need

Install the smee-client in local machine to check the webhook information

To check the information we can use the command line: nc -l 3000

Create a new script to check webhook information in python and also using Node.js client

GitHup APP
Developer Setting

OauthAPP - > using in ci

Where can this GitHub App be installed?
Only on this account -> Only for my account
Any account -> Allow this GitHub App to be installed by any user or organization.

Generate token

Need to install in the repo I want.

This token will no be used for unselected repos

authentication GitHub APP

GITHUB_TOKEN https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#defining-access-for-the-github_token-scopes
Using the workflow the github will use the github_token. and to have access do more features we need to define explicitly in the workflow


