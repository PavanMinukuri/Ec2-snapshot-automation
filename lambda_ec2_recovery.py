import boto3

# ✅ Use the correct region (Mumbai = ap-south-1)
ec2 = boto3.client('ec2', region_name='ap-south-1')

def lambda_handler(event, context):
    # ✅ Your snapshot ID
    snapshot_id = "snap-04a19fec1b079669d"

    # Step 1: Create a volume from the snapshot
    try:
        volume = ec2.create_volume(
            SnapshotId=snapshot_id,
            AvailabilityZone='ap-south-1a', 
            VolumeType='gp2'
        )
        volume_id = volume['VolumeId']
        print(f"Created volume: {volume_id}")
    except Exception as e:
        print(f"Error creating volume: {e}")
        return {
            'statusCode': 500,
            'body': f"Failed to create volume from snapshot {snapshot_id}: {str(e)}"
        }

    # Step 2: Launch a new EC2 instance and attach the volume
    try:
        instance = ec2.run_instances(
            ImageId='ami-019715e0d74f695be',  
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            BlockDeviceMappings=[{
                'DeviceName': '/dev/sdh',
                'Ebs': {
                    'SnapshotId': snapshot_id,
                    'DeleteOnTermination': True,
                    'VolumeType': 'gp2'
                }
            }],
            SubnetId='subnet-0c41120ebf9f3c694',  
            SecurityGroupIds=['sg-0e0011d4d72bca2c4']     
        )
        instance_id = instance['Instances'][0]['InstanceId']
        print(f"Launched instance: {instance_id}")
    except Exception as e:
        print(f"Error launching instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Failed to launch EC2 instance from snapshot {snapshot_id}: {str(e)}"
        }

    return {
        'statusCode': 200,
        'body': f"Restored EC2 instance {instance_id} from snapshot {snapshot_id}"
    }
