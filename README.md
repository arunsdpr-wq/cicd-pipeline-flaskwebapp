# Flask Application CI/CD with GitHub Actions

This project demonstrates a professional CI/CD pipeline using GitHub Actions to automate testing and deployment to AWS EC2 instances.

# Pipeline Logic
1. **Continuous Integration**: On every push to `main` or `staging`, the pipeline installs dependencies and runs `pytest`.
2. **Continuous Deployment (Staging)**: If tests pass on the `staging` branch, code is deployed to the Staging EC2.
3. **Continuous Deployment (Production)**: When a new **Release Tag** is published, the code is deployed to the Production EC2.

# Prerequisites
- **AWS EC2 Instances**: Two instances (Staging & Production) running Ubuntu.
- **Systemd**: Both instances must have a `flaskapp.service` file configured in `/etc/systemd/system/`.
- **Python 3 & Venv**: Installed on the remote servers.

# Required GitHub Secrets
To make this work, add the following secrets in your repository settings:
- `AWS_SSH_KEY`: Your private 'av-secret-key.pem' key.
- `AWS_EC2_IP_STAGING`: (Public IP of Staging server)
- `AWS_EC2_IP_PROD`: (Public IP of Production server)
- `AWS_REMOTE_USER`: Default is `ubuntu`.
