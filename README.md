
# Serverless S3 File Monitoring System

This project implements a serverless solution utilizing AWS Lambda for real-time monitoring of file uploads and deletions within an S3 bucket. The system enhances operational efficiency by providing timely alerts to administrators, enabling proactive issue resolution.

<img width="702" alt="Screen Shot 2024-04-03 at 4 43 12 PM" src="https://github.com/amanuelararso/Serverless-Monitoring-of-AWS-S3-Bucket/assets/26092925/1bc2d769-5211-4469-aa7f-27ba84d74f21">



## Features

- **Real-time Monitoring**: The system continuously tracks changes in the designated S3 bucket, ensuring administrators are promptly notified of any file uploads or deletions.
  
- **Serverless Architecture**: Leveraging AWS Lambda, the solution operates without the need for managing servers, optimizing resource utilization, and reducing infrastructure costs.
  
- **Immediate Alerts**: Integrated with AWS Simple Notification Service (SNS), the system delivers real-time notifications to administrators, enabling swift response to any detected changes.
  
## Implementation Details

- **AWS Lambda**: The core of the solution, AWS Lambda functions are deployed to monitor S3 events and trigger notifications accordingly.
  
- **S3 Bucket**: The designated S3 bucket serves as the repository for file uploads and deletions, which are monitored in real-time.
  
- **Simple Notification Service (SNS)**: Integrated with Lambda functions to deliver immediate alerts to administrators via various communication channels.
  
## Benefits

- **Operational Efficiency**: Administrators receive timely notifications, enabling them to take swift action in response to file uploads or deletions, thereby enhancing operational efficiency.
  
- **Cost Optimization**: Utilizing a serverless architecture with AWS Lambda reduces infrastructure costs by eliminating the need to provision and manage servers.
  
- **Scalability**: The solution scales seamlessly to accommodate varying workloads, ensuring consistent performance regardless of the volume of file activities within the S3 bucket.

## Getting Started

To deploy and configure the system in your AWS environment, follow these steps:

1. **AWS Account Setup**: Ensure you have an AWS account with appropriate permissions to create Lambda functions, S3 buckets, and SNS topics.

2. **Lambda Deployment**: Deploy the provided Lambda functions to your AWS account. Ensure proper configuration, including setting up triggers to monitor S3 events.

3. **S3 Bucket Configuration**: Designate an S3 bucket for file monitoring. Configure event notifications to trigger Lambda functions upon file uploads or deletions.

4. **SNS Integration**: Create an SNS topic and configure subscriptions to receive notifications. Ensure Lambda functions are integrated with the SNS topic for alert delivery.

5. **Testing**: Test the system by uploading and deleting files within the designated S3 bucket. Verify that notifications are delivered promptly to the configured endpoints.

6. **Monitoring and Maintenance**: Regularly monitor the system's performance and ensure proper functioning. Update configurations or scale resources as needed to accommodate changing requirements.

## Contributors

- [Amanuel Ararso](https://github.com/amanuelararso)

## License

This project is licensed under the [MIT License](LICENSE).
