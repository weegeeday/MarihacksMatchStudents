from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

class FormsResp:

    #This gets a google forms ID, to get all of its responses. Requires one auth. Accounts must be added to google cloud.
    @staticmethod
    def GetResp(Id):
        SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
        DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

        store = file.Storage("./Backend/tokenr.json")
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets("./Backend/credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)

        service = discovery.build(
            "forms",
            "v1",
            http=creds.authorize(Http()),
            discoveryServiceUrl=DISCOVERY_DOC,
            static_discovery=False,
        )


        result = service.forms().responses().list(formId=Id).execute()
        return result

    @staticmethod
    def GetForm(Id):
        SCOPES = "https://www.googleapis.com/auth/forms.body"
        DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
        store = file.Storage("./Backend/tokenb.json")
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets("./Backend/credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)

        service = discovery.build(
            "forms",
            "v1",
            http=creds.authorize(Http()),
            discoveryServiceUrl=DISCOVERY_DOC,
            static_discovery=False,
        )
        result = service.forms().get(formId=Id).execute()
        return result