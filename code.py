import json
import glob

result = {}

input_filename = input("Enter starting filename: ")

for f in glob.glob(input_filename + "[0-9].json"):
    with open(f, "rb") as infile:
        data = json.load(infile)
        for k in data:
            if(k not in result):
                result[k] = [data[k]]
            else:
                result[k].append(data[k])


with open("merge1" + ".json", "w") as output_name:
     json.dump(result, output_name)