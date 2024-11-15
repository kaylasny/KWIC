# 读取输入文件内容
def read_input(filename):
    with open(filename, 'r') as file:
        return file.readlines()

# 生成循环移位


def generate_shifts(lines):
    shifts = []
    for line in lines:
        words = line.split()
        for i in range(len(words)):
            shifts.append(' '.join(words[i:] + words[:i]))
    return shifts

# 对循环移位进行排序


def sort_shifts(shifts):
    return sorted(shifts)

# 输出排序结果


def output_result(sorted_shifts):
    for shift in sorted_shifts:
        print(shift)

# 主程序


def main():
    # 读取输入
    lines = read_input('input.txt')

    # 生成循环移位
    shifts = generate_shifts(lines)

    # 排序
    sorted_shifts = sort_shifts(shifts)

    # 输出结果
    output_result(sorted_shifts)


if __name__ == "__main__":
    main()
