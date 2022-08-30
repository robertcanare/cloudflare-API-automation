# Cloudflare API automation script
import argparse
import requests
import json

# Get the user input
parser = argparse.ArgumentParser(description='Cloudflare automation script')
parser.add_argument('--email', required=True, help='User email address')
parser.add_argument('--api', required=True, help='User API key')
parser.add_argument('--domain', required=True, help='Target domain')
parser.add_argument('--task', required=True, help='Options are available on the repository')
parser.add_argument('--value', help='value')
args = parser.parse_args()

# Put value to much presentable variables
cloudflareEmail = args.email
cloudflareToken = args.api
cloudflareDomain = args.domain
cloudflareTasks = args.task
cloudflareValue = args.value

# Variable required on Cloudflare API call
cloudflareURL = "https://api.cloudflare.com/client/v4"
header = {'X-Auth-Email': cloudflareEmail, 'X-Auth-Key': cloudflareToken, 'Content-Type': "application/json"}

# Get the domain zone ID
zoneID = requests.get(url=f"https://api.cloudflare.com/client/v4/zones?name={cloudflareDomain}", headers=header)
jsonElements = json.loads(zoneID.text)
jsonList = str(jsonElements["result"])
removedBrackets = jsonList.strip("[]")
cloudflareDomainId = removedBrackets[8:40]


# Cloudflare tasks and list of available functions
# Get the Proxy read timeout details
def sendGetProxyReadTimeout(domainId):
    r = requests.get(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/settings/proxy_read_timeout",
                     headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Update the Proxy read timeout value
def sendPatchProxyReadTimeout(domainId):
    # Get the value
    dataValue = f"""{{"value":"{cloudflareValue}"}}"""

    r = requests.patch(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/settings/proxy_read_timeout",
                       data=dataValue, headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Get the O2O details
def sendGetO2O(domainId):
    r = requests.get(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/settings/orange_to_orange",
                     headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Update the O2O value
def sendPatchO2O(domainId):
    # Get the value
    dataValue = f"""{{"value":"{cloudflareValue}"}}"""

    r = requests.patch(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/settings/orange_to_orange",
                       data=dataValue, headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Get the SSL verification details
def sendGetSSLVerification(domainId):
    r = requests.get(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/ssl/verification?retry=true",
                     headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Refresh the SSL validation
def sendPatchSSLRefresh(domainId):
    r = requests.patch(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/ssl/verification/{cloudflareValue}",
                       data='{"validation_method":"txt"}', headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Get the Certificate pack details
def sendGetCertPack(domainId):
    r = requests.get(url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/ssl/certificate_packs?status=all",
                     headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Refresh certificate pack
def sendPatchCertPacks(domainId):
    r = requests.patch(
        url=f"https://api.cloudflare.com/client/v4/zones/{domainId}/ssl/certificate_packs/{cloudflareValue}",
        headers=header)
    jsonElement = json.loads(r.text)
    print(jsonElement)


# Check if the user task input is in the current list
if cloudflareTasks == "proxy_read_timeout_details":
    # Proxy read timeout details function
    print(f"""The Proxy read timeout details for {cloudflareDomain}:""")
    sendGetProxyReadTimeout(cloudflareDomainId)

elif cloudflareTasks == "proxy_read_timeout_update":
    print(f"""The Proxy read timeout value for {cloudflareDomain} is changed to {cloudflareValue}:""")
    sendPatchProxyReadTimeout(cloudflareDomainId)

elif cloudflareTasks == "o2o_details":
    # O2O details function
    print(f"""The O2O details for {cloudflareDomain}:""")
    sendGetO2O(cloudflareDomainId)

elif cloudflareTasks == "o2o_update":
    print(f"""The O2O value for {cloudflareDomain} is changed to {cloudflareValue}:""")
    sendPatchO2O(cloudflareDomainId)

elif cloudflareTasks == "ssl_details":
    print(f"""The SSL details for {cloudflareDomain}:""")
    sendGetSSLVerification(cloudflareDomainId)

elif cloudflareTasks == "refresh_verification":
    print(f"""The SSL cert_pack_uuid  value for {cloudflareDomain} is refresh to {cloudflareValue}:""")
    sendPatchSSLRefresh(cloudflareDomainId)

elif cloudflareTasks == "cert_pack_details":
    print(f"""The certificate pack details for {cloudflareDomain}:""")
    sendGetSSLVerification(cloudflareDomainId)

elif cloudflareTasks == "refresh_validation":
    print(f"""The SSL cert_pack_uuid  value for {cloudflareDomain} is changed to {cloudflareValue}:""")
    sendPatchSSLRefresh(cloudflareDomainId)

else:
    print("Your chosen task is not in the current list:"
          "\n"
          "\nTo get the current proxy read timeout value:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task "
          "proxy_read_timeout_details "
          "\n"
          "\nTo set timeout proxy read timeout value:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task "
          "proxy_read_timeout_update --value target-value "
          "\n"
          "\nTo check the current O2O current status:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task o2o_details"
          "\n"
          "\nTo change the O2O value:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task o2o_update "
          "--value target-value "
          "\n"
          "\nTo get the SSL verification details:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task ssl_details"
          "\n"
          "\nTo refresh SSL verification:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task "
          "refresh_verification --value target-cert-pack-uuid "
          "\n"
          "\nTo get the certificate pack details:"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task "
          "cert_pack_details "
          "\n"
          "\nTo refresh certificate packs validation"
          "\npython CF_Automation.py --domain target-domain --email your-email --api your-token --task "
          "refresh_validation --value target-cert-pack-uuid "
          "")
