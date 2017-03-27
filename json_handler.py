import json

class JSONHandler():

    @staticmethod
    def jsonify(loc, ware_list, ware_path_list):

        data_dict = {loc:{k: v for (k,v) in zip(ware_list, ware_path_list)}}

        with open('locationPaths.json', 'w') as fp:
            fp.write(json.dumps(data_dict, sort_keys=True, indent=4))

    def dejsonify(fileName):

        with open('locationPaths.json', 'r') as fp:
            return json.load(fp)
