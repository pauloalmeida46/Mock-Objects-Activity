from exercicio1.src.custom_stack_class import CustomStack


class NumberAscOrder:

    def sort(self, custom_stack):
        if not isinstance(custom_stack, CustomStack):
            raise TypeError("custom_stack deve ser uma instância de CustomStack")

        numbers = []
        while not custom_stack.is_empty():
            numbers.append(custom_stack.pop())

        numbers.sort()
        return numbers
