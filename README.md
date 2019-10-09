# Configure the AppPulse Active Add-On

After installing the Add-On, navigate to the Configuration page.  Click "Add" and complete the following information:
 - Account Name
 - Client Id
 - Client Secret

Under "Add-On Settings" complete the following:
 - SaaS Domain
 - Tenant ID

---

# Adding Inputs

On the Inputs page in the Add-On you can create the following inputs:

## AppPulse Active Application Data
Lists all Azure DevOps Projects

### Sourcetype
    AppPulse_Active:Data
### Endpoint
    GET <SaaS domain>/openapi/rest/v1/<tenant ID>/getData?lastRetrievedSequestID=<x>


## AppPulse Active Configuration
Lists all Release Approvals

### Sourcetype
	AppPulse_Active:Configuration
### Endpoint
	GET <SaaS domain>/openapi/rest/v1/<tenant ID>/getConfiguration

---

# AppPulse Active REST API Reference
[http://apppulse-help.saas.hpe.com/active/eng/Content/4_Open_API/open_API.htm?Highlight=api](http://apppulse-help.saas.hpe.com/active/eng/Content/4_Open_API/open_API.htm?Highlight=api)
