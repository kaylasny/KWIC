import queue


# 共享数据存储
shared_data = {"input": [], "shifts": [], "sorted": []}

# 事件队列
event_queue = queue.Queue()

# 文件名
filename = "input.txt"

# 事件处理器：读取输入文件内容


def handle_read_input():
    with open(filename, 'r') as file:
        shared_data["input"] = file.readlines()
    print("Input file read.")
    # 触发生成循环移位的事件
    event_queue.put("generate_shifts")


# 事件处理器：生成循环移位
def handle_generate_shifts():
    shifts = []
    for line in shared_data["input"]:
        words = line.split()
        for i in range(len(words)):
            shifts.append(' '.join(words[i:] + words[:i]))
    shared_data["shifts"] = shifts
    print("Shifts generated.")
    # 触发排序的事件
    event_queue.put("sort_shifts")


# 事件处理器：对循环移位进行排序
def handle_sort_shifts():
    shared_data["sorted"] = sorted(shared_data["shifts"])
    print("Shifts sorted.")
    # 触发输出结果的事件
    event_queue.put("output_result")


# 事件处理器：输出排序结果
def handle_output_result():
    for shift in shared_data["sorted"]:
        print(shift)
    print("Output completed.")


# 事件驱动的主程序
def main():
    # 初始化事件，读取输入文件
    event_queue.put("read_input")

    # 事件循环
    while not event_queue.empty():
        event = event_queue.get()

        # 使用字典模拟 switch-case
        event_handlers = {
            "read_input": handle_read_input,
            "generate_shifts": handle_generate_shifts,
            "sort_shifts": handle_sort_shifts,
            "output_result": handle_output_result
        }

        # 获取对应的事件处理函数并调用
        handler = event_handlers.get(event)
        if handler:
            handler()
        else:
            print(f"Unknown event: {event}")


if __name__ == "__main__":
    main()
