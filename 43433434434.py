import random
def main():
    list1 = [random.randint(1, 20) for _ in range(10)]
    list2 = [random.randint(1, 20) for _ in range(10)]
    print("Исходные списки:")
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print()
    combinedlist = list1 + list2
    print("Элементы обоих списков:")
    print(combinedlist)
    print()
    uniquecombined = list(set(list1 + list2))
    print("Элементы обоих списков без повторений:")
    print(uniquecombined)
    print()
    commonelements = list(set(list1) & set(list2))
    print("Общие элементы для двух списков:")
    print(commonelements)
    print()
    uniquetolist1 = [x for x in list1 if x not in list2]
    uniquetolist2 = [x for x in list2 if x not in list1]
    alluniqueelements = uniquetolist1 + uniquetolist2
    print("Уникальные элементы каждого из списков:")
    print(alluniqueelements)
    print()
    minmaxlist = [min(list1), max(list1), min(list2), max(list2)]
    print("Минимальное и максимальное значение каждого из списков:")
    print(minmaxlist)
    print()
    print("=" * 50)
    print("детальная информация:")
    print(f"Минимум списка 1: {min(list1)}")
    print(f"Максимум списка 1: {max(list1)}")
    print(f"Минимум списка 2: {min(list2)}")
    print(f"Максимум списка 2: {max(list2)}")
def alternative_solution():
    list1 = [random.randint(1, 15) for _ in range(8)]
    list2 = [random.randint(1, 15) for _ in range(8)]
    print("Альтернативное решение:")
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print()
    def combine_lists(lst1, lst2):
        return lst1 + lst2

    def combine_unique(lst1, lst2):
        return list(set(lst1) | set(lst2))

    def find_common(lst1, lst2):
        return list(set(lst1) & set(lst2))

    def find_unique_elements(lst1, lst2):
        unique1 = set(lst1) - set(lst2)
        unique2 = set(lst2) - set(lst1)
        return list(unique1 | unique2)
    def find_min_max(lst1, lst2):
        return [min(lst1), max(lst1), min(lst2), max(lst2)]
    print("Комбинированный список:", combine_lists(list1, list2))
    print("Без повторений:", combine_unique(list1, list2))
    print("Общие элементы:", find_common(list1, list2))
    print("Уникальные элементы:", find_unique_elements(list1, list2))
    print("Минимумы и максимумы:", find_min_max(list1, list2))
if __name__ == "__main__":
    main()
    print("\n" + "=" * 50)
    alternative_solution()














































































































































































