import json

class JSONHandler():

    @staticmethod
    def jsonify(file_name, loc, ware_list, ware_path_list):

        data_dict = {loc:{k: v for (k,v) in zip(ware_list, ware_path_list)}}

        with open(file_name, 'w') as fp:
            fp.write(json.dumps(data_dict, sort_keys=True, indent=4))

    def dejsonify(file_name):

        with open(file_name, 'r') as fp:
            return json.load(fp)
