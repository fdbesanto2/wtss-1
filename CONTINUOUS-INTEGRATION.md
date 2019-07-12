# Continuous Integration with Jenkins

The CI workflow is available in [`CI - Workflow`](https://drive.google.com/file/d/1QgSeMcNRph6ORE6kDDf_qazYtntqYpKb/view)

We have prepared [`Jenkinsfile`](./Jenkinsfile) containing entire workflow of Brazil Data Cube - Web Time Series Service (WTSS) to represent mainly the integration with GitHub.

## Jenkinsfile

The Jenkinsfile is composed by five six steps that must be strictly followed in order to keep the funcionalities working as expected.
These steps are defined as:

* **prepare environment** which it builds Dockerfile and install Python package dependencies defined in [`requirements.txt`](./requirements.txt). After that, the create image will be used to run the other steps.

* **code-check** Perform static and semantic analysis code to guarantee code quality. The Jenkinsfile is configured to mark build as:
    - `unstable` for any *warning* found with high severity.
    - `failed` when a potential error found.
    - `success` when no entry is found.

* **generate docs** Generate project documentation using `readthedocs` framework. We will provide doc URI in order to Reviewer check before merge.

* **unittest** Run project unittesting on folder `tests`.

* **deploy** Deploy application to respective server context. For Pull Request Integration, the application is deployed to the development server to act like production environment. Once configured, the repository reviewer will check through link available in Pull Request Comment.

When an error occurrs, there is a special handler which will cleanup the built docker images. We also defined integration with `Slack Channel` that will notify the team developers about repository interaction.

### Production

TODO