# 5) Find Count of Most Frequent Item in an Array


def most_frequent_item_count(collection):
    highest = 0
    for element in collection:
        if collection.count(element) >= highest:
            highest = collection.count(element)
    return highest
                    