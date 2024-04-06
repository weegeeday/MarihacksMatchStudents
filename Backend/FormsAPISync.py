import Form2mdb
class FormsSync:

    @staticmethod
    def Sync(Id):
        try:
            Form2mdb.Form2mdb.InsertData(Id)
            return True
        except any:
            return False
        