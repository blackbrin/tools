import crcmod.predefined

# 假设集群配置，其中每个元组代表(开始槽, 结束槽, 节点标识)
cluster_slots = [
    (0, 5460, 'node1'),
    (5461, 10922, 'node2'),
    (10923, 16383, 'node3'),
]

def get_node_by_key(key):
    # 使用crc16算法计算key的哈希值
    crc16 = crcmod.predefined.mkCrcFun('crc-16')
    hash_val = crc16(key.encode()) & 0xFFFF
    slot = hash_val % 16384  # Redis集群有16384个槽

    # 确定键属于哪个节点
    for start_slot, end_slot, node in cluster_slots:
        if start_slot <= slot <= end_slot:
            return node
    return None

# 测试
key = "some_key"
node = get_node_by_key(key)
print(f"Key '{key}' should be in {node}")