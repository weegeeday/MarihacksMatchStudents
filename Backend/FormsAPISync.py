import FormsAPI
import time
class FormsSync:

    @staticmethod
    def Sync(Id):
        try:
            FormsAPI.FormsResp.GetResp(Id)
            return True
        except any:
            return False
        