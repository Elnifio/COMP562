import os, random
import json

def getData(seeds, initial_pattern):
    labels = {"0": "High, decreasing, high, decreasing, high", 
                "1": "decreasing middle, high spike, random decreasing",
                "2": "constantly decreasing", 
                "3": "decreasing phase before the peak"}
    os.makedirs('outputs')

    pattern = initial_pattern
    datas = []
    for seed in seeds:
        os.system("./t %s %s > ./outputs/out%s.txt" % (pattern, seed, seed))
        with open("./outputs/out%s.txt" % seed, 'r') as f:
            contents = f.read().split("\n")
            pattern = contents[0][-1]
            cts = contents[1].replace(" ", "")
            dts = [int(x) for x in cts.split(",")]
            data = {"pattern": int(pattern), "data": dts, 'label': labels[pattern]}
            datas.append(data)
        os.remove("./outputs/out%s.txt" % seed)

    os.removedirs('outputs')
    patterns = [x['pattern'] for x in datas]
    original_datas = [x['data'] for x in datas]
    out = {"initial_pattern": initial_pattern, 'datas': datas}
    return out, patterns, original_datas


# x = json.dumps(getData([random.randint(0, 999) for x in range(10)], [1, ]))
# with open("out.txt", 'w') as f:
#     f.write(x)

# x = [random.randint(0, 99) for x in range(10)]
# pattern = '0'
# os.makedirs("outputs")
# patterns = [pattern, ]
# datas = []
# labels = {"0": "High, decreasing, high, decreasing, high", 
#                 "1": "decreasing middle, high spike, random decreasing",
#                 "2": "constantly decreasing", 
#                 "3": "decreasing phase before the peak"}

# for i in x:
#     os.system("./t %s %s > ./outputs/out%s.txt" % (pattern, i, i))
#     with open("./outputs/out%s.txt" % i, 'r') as f:
#         contents = f.read().split("\n")
#         pattern = contents[0][-1]
#         dts = contents[1]
#         data = {'pattern': pattern, "data": dts}
#         datas.append(data)
#         patterns.append(pattern)
#     os.remove('./outputs/out%s.txt' % i)

# os.removedirs('outputs')

# print("--------")
# print(patterns)
# for item in datas:
#     print(item, ": ", labels[item['pattern']])

