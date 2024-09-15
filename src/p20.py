from collections import Counter
import math


def info_entropy(labels):
    label_count = Counter(labels)
    total = len(labels)
    entropy = sum(
        -count/total*math.log2(count/total) for count in label_count.values()
        )
    return entropy


def info_gain(data: list[dict], label, target_label):
    info_ent = info_entropy([example[label] for example in data])
    target_counter = Counter([example[target_label] for example in data])
    cond_entropy = 0
    for target, target_count in target_counter.items():
        target_info_ent = info_entropy([
            data_attr[label] for data_attr in data
            if data_attr[target_label] == target
            ])
        cond_entropy += target_info_ent * target_count / len(data)
    return info_ent - cond_entropy


def max_info_gain(data: list[dict], attributes: list[str], target_attr: str):
    info_gain_l = [info_gain(data, target_attr, attr) for attr in attributes]
    return attributes[info_gain_l.index(max(info_gain_l))]


def learn_decision_tree(
        examples: list[dict], attributes: list[str], target_attr: str
        ) -> dict:
    if info_entropy([example[target_attr] for example in examples]) == 0:
        return examples[0][target_attr]
    node_attr = max_info_gain(examples, attributes, target_attr)
    target_list = [example[node_attr] for example in examples]
    decision_tree = {node_attr: {key: None for key in target_list}}
    if len(decision_tree[node_attr]) == 1:
        return examples[0][target_attr]
    for node_key in decision_tree[node_attr].keys():
        sub_examples = [
            example for example in examples if example[node_attr] == node_key]
        decision_tree[node_attr][node_key] = learn_decision_tree(
            sub_examples, attributes, target_attr)
    return decision_tree
