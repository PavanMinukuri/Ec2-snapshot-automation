# Ec2-snapshot-automation
# Ec2-snapshot-automation
AWS-ec2-snapshot-restore

## Restore EC2 Instance from Snapshot using AWS Lambda

Here’s my flowchart diagram for the assignment — it visually explains the workflow:

## EC2 Instance → EBS Volume → Snapshot → Lambda → New EC2 Instance
<img width="733" height="475" alt="image" src="https://github.com/user-attachments/assets/8ae3eb02-0985-4542-866e-57df8bf8c63f" />


### Overview
This project demonstrates how to **automate EC2 instance recovery** using AWS Lambda.  
The workflow restores an EC2 instance from a given **EBS snapshot** by:
1. Creating a new EBS volume from the snapshot.
2. Launching a new EC2 instance in the specified region.
3. Attaching the restored volume to the new instance.

---

### Prerequisites
- AWS account with permissions to use EC2, Lambda, and CloudWatch.
- At least one **EBS snapshot** available (used for restoration).
- IAM role with:
  - `AmazonEC2FullAccess`
  - `CloudWatchLogsFullAccess`
- Python 3.14 runtime for Lambda.
<img width="1276" height="619" alt="image" src="https://github.com/user-attachments/assets/ac2781ca-95f8-4919-8604-6ef3f46577a3" />


---

## Steps

### 1. Create IAM Role
- Go to **IAM → Roles → Create role**.
- Select **Lambda** as trusted entity.
- Attach policies:
  - `AmazonEC2FullAccess`
  - `CloudWatchLogsFullAccess`
- Name the role: `LambdaEC2SnapshotRole`.
<img width="940" height="461" alt="image" src="https://github.com/user-attachments/assets/5183a982-7122-4d4f-be03-ca1dccf45fe0" />

---

### 2. Create Lambda Function
- Go to **Lambda → Create function (Lambda-EC2SnapshotFunction)**.
- Runtime: **Python 3.14**.
- Execution role: **Use existing role → LambdaEC2SnapshotRole**.
<img width="940" height="453" alt="image" src="https://github.com/user-attachments/assets/b97d106d-d4ad-4609-b51f-76d44b194df7" />

---

### 3. Add Python Code
Save the following code as `lambda_ec2_recovery.py`.
Run the code & New instance will get created.
Code result after running it:
<img width="940" height="399" alt="image" src="https://github.com/user-attachments/assets/df6ef86b-beaf-49e9-90f7-2b2f5da16d52" />


New Instance got created in ap-south-1 region:
<img width="1273" height="618" alt="image" src="https://github.com/user-attachments/assets/140fcdda-47d5-47f5-ab29-ef83435061c6" />
<img width="1273" height="585" alt="image" src="https://github.com/user-attachments/assets/c9547ae1-ef65-45b0-a9d4-c9f99fcab6c7" />



