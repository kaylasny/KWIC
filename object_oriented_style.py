class KWICSystem:
    def __init__(self):
        self.input_handler = InputHandler()
        self.circular_shift_generator = CircularShiftGenerator()
        self.sorter = Sorter()
        self.output_handler = OutputHandler()

    def run(self, filename):
        lines = self.input_handler.read_input(filename)
        shifts = self.circular_shift_generator.generate_shifts(lines)
        sorted_shifts = self.sorter.sort_shifts(shifts)
        self.output_handler.output_result(sorted_shifts)


class InputHandler:
    def read_input(self, filename):
        with open(filename, 'r') as file:
            return file.readlines()


class CircularShiftGenerator:
    def generate_shifts(self, lines):
        shifts = []
        for line in lines:
            words = line.split()
            for i in range(len(words)):
                shifts.append(' '.join(words[i:] + words[:i]))
        return shifts


class Sorter:
    def sort_shifts(self, shifts):
        return sorted(shifts)


class OutputHandler:
    def output_result(self, sorted_shifts):
        for shift in sorted_shifts:
            print(shift)


# 执行 KWIC 系统
kwic_system = KWICSystem()
kwic_system.run('input.txt')
