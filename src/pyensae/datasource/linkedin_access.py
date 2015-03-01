"""
@file
@brief provides functionalities around `LinkedIn <http://fr.linkedin.com/>`_.

Some pointers:
   - `API LinkedIn <http://developer.linkedin.com/rest>`_
   - `examples with LinkedIn API <http://developer.linkedin.com/apis>`_
   - `using oauth <https://developer.linkedin.com/documents/getting-oauth-token-python>`_

Existing Python libraries:
   - `python-linkedin <https://github.com/ozgur/python-linkedin>`_
   - `linkedin-client-library <https://github.com/mrgaaron/LinkedIn-Client-Library>`_

.. require: requests_oauthlib

You should install: `sdpython/python-linkedin <https://github.com/sdpython/python-linkedin>`_

"""
import collections
import datetime
import urllib
import copy
from pyquickhelper import fLOG


class LinkedInAccess:

    """
    This class manages the access to LinkedIn functionalities.

    It assumes you requested an access to the `API LinkedIn <http://developer.linkedin.com/rest>`_
    See also  `ipython + python-linkedin <http://nbviewer.ipython.org/urls/raw.github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/master/ipynb/Chapter%203%20-%20Mining%20LinkedIn.ipynb>`_

    See `linkedin <https://github.com/andrewychoi/python3-linkedin>`_, `linkedin <https://github.com/ozgur/python-linkedin>`_.
    This class proposes simplified versions of the same methods, you should follow those link to see what is missing.

    About LinkedIn:
       -  Throttle limits: see `throttle-limits <http://developer.linkedin.com/documents/throttle-limits>`_
       - To see your API usage: `API limits <https://www.linkedin.com/secure/developer>`_
       - Setting up your `Permissions <https://developer.linkedin.com/documents/authentication#granting>`_
       - `Developing page <https://developer.linkedin.com/whydevelop>`_
       - `Connections API <http://developer.linkedin.com/documents/connections-api>`_
       - `Extend your throttle limits <http://developer.linkedin.com/themes/linkedin-home/form-api.html>`_
       - `Accounts <http://www.linkedin.com/mnyfe/subscriptionv2?displaySalesProduct=&identify=false&crm=sfdc>`_
       - `Accounts comparison <http://www.linkedin.com/mnyfe/subscriptionv2?displayProducts=&family=general&commpare_acct=>`_

    Search API::

        https://api.linkedin.com/v1/company-search:(companies:(id,name,logo_url))?keywords=keyword?oauth2_access_token={accesstoken}&format=json

    @example(How to Get data from your linkedin profile?)

    Search and get profiles:

    @code
    accessToken = [ "w....",
                "n....",
                "3....",
                "2..." ]

    linkedin = LinkedInAccess (*TestLinkedIn.accessToken)
    linkedin.connect()
    se = linkedin.search_profile ( params = {"last-name":"dupre", "first-name":"xavier"} )
    for _ in se["people"]["values"] :
        print(_)
    @endcode

    Same results in a DataFrame:

    @code
    accessToken = [ "w....",
                "n....",
                "3....",
                "2..." ]

    linkedin = LinkedInAccess (*TestLinkedIn.accessToken)
    linkedin.connect()

    df = linkedin.search_profile (
                    params = {"keywords":"ensae"},
                    count = 500,
                    as_df = True )
    @endcode
    @endexample

    """

    default_selectors_profile = ['id',
                                 'first-name',
                                 'last-name',
                                 'location',
                                 'distance', 'num-connections', 'skills',
                                 'educations',
                                 #'school-name',
                                 ]

    default_selectors_search_profile = [
        {'people': ['id',
                    'first-name',
                    'last-name',
                    'educations',
                    #'school-name',
                    'public-profile-url',
                    'location', 'headline',
                    'last-modified-timestamp',
                    'date-of-birth',
                    'member-url-resources',
                    'email-address',
                    ]}]

    def __init__(self, api_key,
                 secret_key,
                 user_token,
                 user_secret):
        """
        constructor, all the following parameter are given when you request an access
        to linkedin

        @param      api_key         api key ``[a-z0-9]+``
        @param      secrect_key     secret key ``[A-Za-z]+``
        @param      user_token      user token ``guid style``
        @param      user_secret     user_secret ``guid style``
        """

        self.api_key = api_key
        self.secret_key = secret_key
        self.user_token = user_token
        self.user_secret = user_secret

    def connect(self, all_permissions=True):
        """
        open the connection to linkedin (using the api_key and the secret_key)

        @param      all_permissions         True to get all permissions, otherwise, only public profiles
        @return                             client
        """
        from linkedin import linkedin
        permissions = linkedin.PERMISSIONS.enums.values() if all_permissions \
            else linkedin.PERMISSIONS.BASIC_PROFILE
        self.authentication = linkedin.LinkedInDeveloperAuthentication(
            self.api_key,
            self.secret_key,
            self.user_token,
            self.user_secret,
            "http://localhost:8000/",
        )

        self.application = linkedin.LinkedInApplication(self.authentication)
        self.all_permissions = all_permissions
        return self.application

    def get_profile(self, selectors=None, id=None, url=None):
        """
        returns the profile of the connected user,

        see `selectors <http://developer.linkedin.com/documents/profile-api>`_ to get the full of allowed selectors.

        @param      selectors       if None, it is replace by ``LinkedInAccess.default_selectors``
        @param      id              search by id
        @param      url             search by url
        @return     json
        """
        if selectors is None and self.all_permissions:
            selectors = LinkedInAccess.default_selectors_profile
        return self.application.get_profile(selectors=selectors,
                                            member_id=id, member_url=url)

    def search_profile(self, params,
                       selectors=None,
                       count=10,
                       as_df=False,
                       start=0):
        """
        search profiles on linkedin, allowed parameters (replace _ by -):
            - first-name
            - last-name

        The others fields are (see `search api <http://developer.linkedin.com/documents/people-search-api>`_ ::

                http://api.linkedin.com/v1/people-search?
                    keywords=[space delimited keywords]&
                    first-name=[first name]&
                    last-name=[last name]&
                    company-name=[company name]&
                    current-company=[true|false]&
                    title=[title]&
                    current-title=[true|false]&
                    school-name=[school name]&
                    current-school=[true|false]&
                    country-code=[country code]&
                    postal-code=[postal code]&
                    distance=[miles]&
                    start=[number]&
                    count=[1-25]&
                    facet=[facet code, values]&
                    facets=[facet codes]&
                    sort=[connections|recommenders|distance|relevance]

        @param      params          dictionary ``{ field: value }`` (see above)
        @param      selectors       if None, uses the default selectors
        @param      count           1 to 25, if -1 or > 25, search for all (do multiple searches and concatenate them
        @param      as_df           return a DataFrame
        @param      start           first result to fetch
        @return                     json format (or DataFrame if as_df is True or None if there is nothing to return)

        Example of code:

            @code
            accessToken = [ "w....",
                        "n....",
                        "3....",
                        "2..." ]

            linkedin = LinkedInAccess (*TestLinkedIn.accessToken)
            linkedin.connect()
            se = linkedin.search_profile ( params = {"last-name":"dupre", "first-name":"xavier"} )
            for _ in se["people"]["values"] :
                print(_)
            @endcode

        """
        from linkedin import linkedin
        if selectors is None and self.all_permissions:
            selectors = LinkedInAccess.default_selectors_search_profile

        bound = count if count != -1 and count <= 25 else 25
        params = copy.copy(params)
        params["count"] = bound
        params["start"] = start

        if 0 <= count <= 25:
            res = self.application.search_profile(
                selectors=selectors,
                params=params)
            if as_df:
                if len(res) == 1:
                    key, first = res.popitem()
                    values = first["values"]
                    import pandas
                    return pandas.DataFrame(values)
                else:
                    raise Exception(
                        "expecting a result such as {'people': ...}")
            else:
                return res

        else:
            res = []
            start = 0
            total = 0
            while True:
                params["start"] = start
                try:
                    se = self.application.search_profile(
                        selectors=selectors,
                        params=params)
                except linkedin.LinkedInError as e:
                    if "Throttle limit" in str(e):
                        fLOG(e)
                    break

                if len(se) == 1:
                    key, first = se.popitem()
                    fetched = first.get("_count", 0)
                    total += fetched
                    alls = first.get("_total", 0)
                else:
                    raise Exception(
                        "expecting a result such as {'people': ...} +\n" +
                        str(se))

                if as_df:
                    values = first.get("values", [])
                    res.extend(values)
                else:
                    res.append(se)

                fLOG(
                    "LinkedInAccess.search_profile [bound=%d,count=%d,fetched=%d,total=%d,alls=%d]" %
                    (bound, count, fetched, total, alls))
                if fetched < bound or (count != -1 and len(res) >= count):
                    break
                start = total

            if as_df:
                if len(res) > 0:
                    import pandas
                    return pandas.DataFrame(res)
                else:
                    return None
            else:
                return res

    def get_connections(self, member_id=None,
                        member_url=None,
                        selectors=None,
                        params=None):
        """
        retrieve the connection for a given profile

        @param      member_id       member id (id or url)
        @param      member_url      member url (id or url)
        @param      selectors       fields to select (@see me search_profile)
        @param      params          parameters
        @return                     list of connections

    Example of code:

        @code
        accessToken = [ "w....",
                    "n....",
                    "3....",
                    "2..." ]

        linkedin = LinkedInAccess (*TestLinkedIn.accessToken)
        linkedin.connect()
        profile = linkedin.get_profile()
        connections = linkedin.get_connection(member_id = profile["id"])

        for conn in connections["values"] :
            print (conn)
        @endcode
        """
        res = self.application.get_connections(
            member_id=member_id,
            member_url=member_url,
            selectors=selectors,
            params=params)
        return res
