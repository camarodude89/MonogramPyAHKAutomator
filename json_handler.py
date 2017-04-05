import json

class JSONHandler():

    @staticmethod
    def jsonify(filename, loc, ware_list, ware_path_list):

        data_dict = {loc:{k: v for (k,v) in zip(ware_list, ware_path_list)}}

        with open(filename, 'w') as fp:
            fp.write(json.dumps(data_dict, sort_keys=True, indent=4))

    @staticmethod
    def dejsonify(filename):

        with open(filename, 'r') as fp:
            return json.load(fp)
