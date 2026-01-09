class Record:

    def __init__(self, pathName, csvId):
        self.profileId = pathName
        self.csdvId = csvId

    @property
    def getPath(self):
        return 'Path : {}'.format(self.pathName)
    
    @property
    def getId(self):
        return 'Id : {}'.format(self.csdvId)