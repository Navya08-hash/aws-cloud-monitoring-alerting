\# AWS Cloud Monitoring \& Alerting System



A cloud-based monitoring and alerting project that deploys a Python Flask application on Amazon EC2 and monitors its CPU utilization using Amazon CloudWatch. When CPU utilization crosses the configured threshold, a CloudWatch Alarm triggers Amazon SNS to send an email notification.



\## Architecture



```text

&#x20;                   AWS Cloud

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │      EC2        │

&#x20;             │  Amazon Linux   │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                   systemd

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │ Flask           │

&#x20;             │ Application     │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                CPU Utilization

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │   CloudWatch    │

&#x20;             │     Metrics     │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                 CPU > 70%

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │ CloudWatch      │

&#x20;             │ Alarm           │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │      SNS        │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;                 Email Alert

````



\## Project Overview



The objective of this project was to deploy a Flask application on AWS EC2 and build a basic cloud monitoring and alerting workflow.



The application includes endpoints for:



\* Application homepage

\* Health checking

\* Error simulation

\* CPU workload generation



Amazon CloudWatch monitors the EC2 CPU utilization, while a CloudWatch Alarm detects high CPU usage. Amazon SNS is used to send an email notification when the alarm enters the `ALARM` state.



\## Technologies Used



\* \*\*AWS EC2\*\* — Application hosting

\* \*\*Amazon CloudWatch\*\* — Infrastructure monitoring

\* \*\*CloudWatch Alarm\*\* — CPU threshold monitoring

\* \*\*Amazon SNS\*\* — Email notifications

\* \*\*Amazon Linux\*\* — EC2 operating system

\* \*\*Python\*\* — Application development

\* \*\*Flask\*\* — Web framework

\* \*\*systemd\*\* — Linux service management

\* \*\*SSH / SCP\*\* — Remote access and file transfer

\* \*\*Git / GitHub\*\* — Version control



\## Application Endpoints



| Endpoint  | Purpose                                               |

| --------- | ----------------------------------------------------- |

| `/`       | Displays the application homepage                     |

| `/health` | Displays application health information and timestamp |

| `/error`  | Generates a test application error and logs it        |

| `/load`   | Generates CPU workload for approximately 10 seconds   |



\## Deployment



\### 1. Launch EC2



An Amazon Linux EC2 instance was created and configured with appropriate security group rules.



SSH access was restricted to my IP address.



\### 2. Set up Python Environment



A Python virtual environment was created on the EC2 instance to isolate project dependencies.



```bash

python3 -m venv venv

source venv/bin/activate

```



Flask was then installed in the virtual environment.



\### 3. Transfer Application



The Flask project was transferred from the local Windows machine to the EC2 instance using SCP.



\### 4. Run Flask



The application listens on:



```text

0.0.0.0:5000

```



This allows the application to accept connections through the EC2 network interface.



\## systemd Service



Instead of manually running the Flask application through an SSH session, a systemd service was configured.



The service:



\* Starts the Flask application automatically

\* Runs the application using the Python virtual environment

\* Restarts the application if it exits unexpectedly

\* Allows the application to continue running after the SSH session is closed



Service name:



```text

flask-monitor.service

```



The service was verified with:



```bash

sudo systemctl status flask-monitor

```



and confirmed to be:



```text

Active: active (running)

```



\## CloudWatch Monitoring



Amazon CloudWatch was configured to monitor the EC2 instance's:



```text

CPUUtilization

```



A CloudWatch Alarm was created with the final threshold:



```text

CPUUtilization > 70%

```



for:



```text

1 datapoint within 5 minutes

```



\## CPU Load Testing



The `/load` endpoint intentionally generates CPU workload for approximately 10 seconds.



This was used to test the monitoring workflow:



```text

/load

&#x20;  ↓

EC2 CPU utilization increases

&#x20;  ↓

CloudWatch detects the CPU change

&#x20;  ↓

Alarm threshold is crossed

&#x20;  ↓

Alarm changes from OK → ALARM

```



\## SNS Email Alert



Amazon SNS was configured as the notification target for the CloudWatch Alarm.



The SNS email subscription was confirmed, and the complete notification workflow was successfully tested.



```text

EC2 CPU increase

&#x20;      ↓

CloudWatch

&#x20;      ↓

CloudWatch Alarm

&#x20;      ↓

SNS

&#x20;      ↓

Email Notification

```



\## Testing \& Validation



The project was tested end-to-end.



\### Application Testing



\* Flask homepage accessed successfully

\* `/health` endpoint tested

\* `/error` endpoint tested

\* `/load` endpoint used to generate CPU workload



\### Infrastructure Testing



\* EC2 instance status checks passed

\* SSH connectivity verified

\* Security group configuration tested

\* Flask application remained accessible after closing the SSH session



\### Monitoring Testing



\* CPU utilization spike observed in CloudWatch

\* CloudWatch Alarm transitioned from `OK` to `ALARM`

\* SNS notification was triggered

\* Email alert was successfully received

\* Alarm returned to `OK` after CPU utilization decreased



\## Screenshots



\### EC2 Instance



!\[EC2 Instance](screenshots/ec2-instance.png)



\### Flask Application



!\[Flask Application](screenshots/flask-app.png)



\### CloudWatch CPU Metric



!\[CloudWatch CPU Metric](screenshots/cloudwatch-cpu.png)



\### CloudWatch Alarm



!\[CloudWatch Alarm](screenshots/cloudwatch-alarm.png)



\### SNS Email Alert



!\[SNS Email Alert](screenshots/sns-email.png)



\### systemd Service



!\[systemd Service](screenshots/systemd-service.png)



\## Key Learnings



Through this project, I gained hands-on experience with:



\* Deploying applications on AWS EC2

\* Linux server administration

\* SSH and SCP

\* Python virtual environments

\* Flask application deployment

\* systemd service management

\* CloudWatch metrics

\* CloudWatch alarms

\* SNS notifications

\* Security group configuration

\* Cloud monitoring and troubleshooting



\## Future Improvements



Potential improvements include:



\* Sending Flask application logs to CloudWatch Logs

\* Adding application uptime monitoring

\* Creating a CloudWatch dashboard

\* Adding an Application Load Balancer

\* Implementing automated deployment using CI/CD

\* Adding more infrastructure metrics

\* Containerizing the Flask application with Docker



\## Project Outcome



The final system successfully demonstrates a complete cloud monitoring workflow:



```text

Deploy Application

&#x20;      ↓

Monitor Infrastructure

&#x20;      ↓

Detect Abnormal CPU Usage

&#x20;      ↓

Trigger CloudWatch Alarm

&#x20;      ↓

Send SNS Notification

&#x20;      ↓

Receive Email Alert

```



This project provided practical experience in AWS infrastructure deployment, monitoring, Linux service management, and automated alerting.



````



