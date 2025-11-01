# lambda-cicd

This repository showcases a simple CI/CD pipeline for deploying a Python-based Lambda function using GitHub Actions and CloudFormation.

## Key Features & Benefits

*   **Automated Deployment:** Streamlines the deployment process using GitHub Actions.
*   **Infrastructure as Code:** Defines infrastructure using CloudFormation for consistent and repeatable deployments.
*   **Version Control:** Leverages Git for tracking changes and collaboration.
*   **CloudFormation Validation:** Validates CloudFormation templates before deployment.

## Prerequisites & Dependencies

*   **AWS Account:** An active AWS account is required.
*   **AWS CLI:** The AWS Command Line Interface (CLI) should be installed and configured with appropriate credentials.
*   **Python 3.6+:** Python 3.6 or higher must be installed to run the Lambda function locally.
*   **Git:** Git must be installed for version control.
*   **GitHub Account:** A GitHub account to store your repository.

## Installation & Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Snarvid82/lambda-cicd.git
    cd lambda-cicd
    ```

2.  **Configure AWS Credentials:**
    Ensure your AWS CLI is configured with appropriate credentials that have permissions to create and update CloudFormation stacks, S3 buckets, and Lambda functions.  You can configure this using:
    ```bash
    aws configure
    ```

3. **Lambda Dependencies (Optional):** Although the requirements.txt is currently empty, to simulate package installations do the following.

    ```bash
    cd lambda
    python3 -m venv .venv
    source .venv/bin/activate # or .venv\Scripts\activate on Windows
    pip install -r requirements.txt # if you were to have dependencies
    cd ..
    ```

4.  **GitHub Secrets:**  Create the following GitHub secrets in your repository settings:

    *   `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
    *   `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
    *   `AWS_REGION`: Your AWS region (e.g., `us-east-1`).

## Usage Examples

The repository includes the following key files:

*   `lambda/lambda_function.py`:  The Lambda function code.
    ```python
    import json

    def lambda_handler(event, context):
        return {
            'statusCode': 200,
            'body': json.dumps('Hello updated lambda from vscode no 3')
        }
    ```
*   `cloudformation/s3-bucket.yml`: CloudFormation template for creating an S3 bucket.
*   `cloudformation/lambda.yml`: CloudFormation template for creating the Lambda function and necessary IAM roles.
*   `.github/workflows/cfn-validate-pr.yml`:  GitHub Actions workflow to validate CloudFormation templates on pull requests.
*   `.github/workflows/lambda.yml`: GitHub Actions workflow to deploy the Lambda function.

To trigger a deployment:

1.  **Make a change to the `lambda/lambda_function.py` file.**
2.  **Commit and push the changes to the `main` branch.**
    ```bash
    git add .
    git commit -m "Update Lambda function"
    git push origin main
    ```

This will trigger the `lambda.yml` GitHub Actions workflow, which will:

*   Validate the CloudFormation template.
*   Package the Lambda function code.
*   Deploy the CloudFormation stack, creating or updating the Lambda function.

## Configuration Options

*   **AWS Region:** The AWS region is configured through the `AWS_REGION` GitHub secret.
*   **S3 Bucket Name:** The S3 bucket name in `cloudformation/s3-bucket.yml` can be modified. Ensure the name is globally unique.
*   **Lambda Function Configuration:** The Lambda function configuration (e.g., memory, timeout) can be adjusted in the `cloudformation/lambda.yml` file.

## Contributing Guidelines

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License Information

This project does not specify a license. All rights are reserved by the owner.

## Acknowledgments

*   This project utilizes GitHub Actions for CI/CD.
*   This project uses CloudFormation for infrastructure as code.
