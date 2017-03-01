import json

class JSONHandler():

    @staticmethod
    def jsonify(loc, wareList, warePathList):

        dataDict = {loc:{k: v for (k,v) in zip(wareList, warePathList)}}

        with open('locationPaths.json', 'w') as fp:
            fp.write(json.dumps(dataDict, sort_keys=True, indent=4))
