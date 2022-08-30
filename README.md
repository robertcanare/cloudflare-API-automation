# Cloudflare Automation Script

# How to use it

## Get the current proxy read timeout value
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task proxy_read_timeout_details`

## Set timeout proxy read timeout value
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task proxy_read_timeout_update --value target-value`

## Check the current O2O current status
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task o2o_details`

## Change the O2O value
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task o2o_update --value target-value`

## Get the SSL verification details
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task ssl_details`

## SSL verification refresh
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task refresh_verification --value target-cert-pack-uuid`

# Get the certificate pack details
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task cert_pack_details`

# Refresh certificate packs validation
`python CF_Automation.py --domain target-domain --email your-email --api your-token --task refresh_validation --value target-cert-pack-uuid`


