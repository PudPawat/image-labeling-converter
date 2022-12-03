import json


main_json = "output/seg.json"
main_json = "sample.json"
main = open(main_json)
main_data = json.load(main)


next_json_path = "output/seg_copy.json"
next_json = open(next_json_path)
next_data = json.load(next_json)
# print(main)
# print(main_data)
# print(type(main_data))

# print(type(main_key))
# print(main_data.keys())

def combincoco_same_cat(main_json, next_json_path):
    main = open(main_json)
    main_data = json.load(main)

    next_json = open(next_json_path)
    next_data = json.load(next_json)

    main_key = list(main_data.keys())
    for key in main_key:
        # print(key)
        # print(main_data[key])
        print("------"*3)

        if key == "images":
            # print(main_data[key])
            # print(type(main_data[key]))
            last_id_main = int(main_data[key][-1]["id"])
            # print(last_id_main)
            # last_id_main = int(last_id_main)

            for i,item_image in enumerate(next_data[key]):
                # print(item_image)
                item_image["id"] = last_id_main +i +1
                print(item_image)
                # print("-----")
                main_data[key].append(item_image)


        if key == "annotations":
            print(key)
            print("-----")
            print(len(main_data[key]))
            print(len(next_data[key]))
            print(main_data[key][1])
            print(next_data[key][-1])
            for j, segment in enumerate(next_data[key]):
                # print(segment)
                segment["image_id"] = last_id_main + segment["image_id"] +1
                # print(segment)
                # break
                main_data[key].append(segment)

            print(main_data[key][-1])
            print(len(main_data[key]))


    # print(main_data["images"]) # TO check images
    json_object = json.dumps(main_data, indent=4)


    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

def get_if_from_list(ele, list):
    for i, element in enumerate(list):
        if ele == element:
            break
    return i

def get_supercategories_list(dicts, key):
    supercat_in_main = []
    for cat in dicts[key]:
        supercat_in_main.append(cat["supercategory"])


def combincoco_universal(main_json, next_json_path):
    main = open(main_json)
    main_data = json.load(main)

    next_json = open(next_json_path)
    next_data = json.load(next_json)

    main_key = list(main_data.keys())
    for key in main_key:
        print("------" * 3)

        if key == "images":
            last_id_main = int(main_data[key][-1]["id"])

            for i, item_image in enumerate(next_data[key]):
                # print(item_image)
                item_image["id"] = last_id_main + i + 1
                print(item_image)
                # print("-----")
                main_data[key].append(item_image)

        if key == "categories":
            correct_ids = []
            ## main
            supercat_in_main = []
            for cat in main_data[key]:
                supercat_in_main.append(cat["supercategory"])

            print("supercat_in_main",supercat_in_main)
            print(main_data[key])
            for cat in next_data[key]:

                if cat["supercategory"] in supercat_in_main:
                    cat_index = get_if_from_list(cat["supercategory"], supercat_in_main)
                    print(cat["id"])
                    main_data[key][cat_index]["correctid"] = cat["id"]
                    correct_ids.append([cat["id"],main_data[key][cat_index]["id"]])

                else:
                    cat["id"] = len(supercat_in_main) + 1
                    cat["correctid"] = cat["id"]
                    supercat_in_main.append(cat["supercategory"])
                    main_data[key].append(cat)
                # print(cat["supercategory"])
                # print(cat["name"])

            print("supercat_in_main",supercat_in_main)
            print(next_data[key])
            print(correct_ids)
            # print("maindata cat",main_data[key])




        if key == "annotations":
            # print(key)
            # print("-----")
            # print(len(main_data[key]))
            # print(len(next_data[key]))
            # print(main_data[key][1])
            # print(next_data[key][-1])
            for j, segment in enumerate(next_data[key]):


                # print(segment)
                segment["image_id"] = last_id_main + segment["image_id"] + 1


                ## correct segment id
                for id, correct_id in correct_ids:
                    print(id,correct_id)
                    if id == segment["category_id"]:
                        segment["category_id"] = correct_id
                        break


                # print(segment)
                # break
                main_data[key].append(segment)

            # print(main_data[key][-1])
            # print(len(main_data[key]))

    # print(main_data["images"]) # TO check images
    json_object = json.dumps(main_data, indent=4)

    with open("sample.json", "w") as outfile:
        outfile.write(json_object)


if __name__ == '__main__':
    combincoco_universal(main_json,next_json_path)