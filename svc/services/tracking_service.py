"""
 package tracking service to track packages using the carriers service provider
 such as 17track API or easyship API, shopify etc..

 Another approach for this service could be using AWS-lambda to fetch a bulk of package status periodically
 and updating our DB with latest status.

Side note:
 In case we wish to integrate carriers ourselves than it will require a dedicated package
 with several modules init such as:
   1. carriers (plugins or API integrations)

"""


def get_package_status_from_carrier(carrier_id, carrier_token, package_id, address):
    # return PackageStatus or None
    pass


