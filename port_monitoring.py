import boto3

def main():
    # Get a list of all AWS regions
    regions = [region['RegionName'] for region in boto3.client('ec2',region_name='us-east-1').describe_regions()['Regions']]

    for region in regions:
        # Call close_port_in_security_group for each region
        close_port_in_security_group(region)
def close_port_in_security_group(region_name):
    ec2 = boto3.client('ec2', region_name=region_name)

    # Get a list of all security groups in the specified region.
    security_groups = ec2.describe_security_groups()['SecurityGroups']

    # Iterate over each security group and check for open ports.
    for security_group in security_groups:
        ingress_rules = security_group['IpPermissions']
        ingress_rule_list = []

        if ingress_rules:
            for rule in ingress_rules:
                from_port = rule.get('FromPort', -1)
                to_port = rule.get('ToPort', -1)
                ip_protocol = rule.get('IpProtocol', None)
                ip_ranges = rule.get('IpRanges', [])
                ingress_rule_list.append({
                    'FromPort': from_port,
                    'ToPort': to_port,
                    'IpProtocol': ip_protocol,
                    'IpRanges': ip_ranges
                })
            print(ingress_rule_list)

            try:
                # Revoke the specified ingress rules for the port.
                ec2.revoke_security_group_ingress(GroupId=security_group['GroupId'], IpPermissions=ingress_rule_list)
                print(f'Successfully revoked ingress rules in security group {security_group["GroupId"]} in region {region_name}')
            except Exception as e:
                print(f'Error revoking ingress rules in security group {security_group["GroupId"]} in region {region_name}: {e}')
        else:
            print(f'No ingress rules found in the security group {security_group["GroupId"]} in region {region_name}')

if __name__ == '__main__':
    main()
