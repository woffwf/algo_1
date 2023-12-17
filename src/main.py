def boyer_moore_search(haystack, needle):

    def calculate_shift_table(needle):
        shift_table = {}
        needle_length = len(needle)


        for i in range(needle_length - 1):
            shift_table[needle[i]] = needle_length - 1 - i

        return shift_table


    def find_match_at_index(index):
        needle_index = len(needle) - 1


        while needle_index >= 0 and needle[needle_index] == haystack[index + needle_index]:
            needle_index -= 1


        return needle_index == -1

    haystack_length = len(haystack)
    needle_length = len(needle)
    shift_table = calculate_shift_table(needle)

    index = 0
    while index <= haystack_length - needle_length:

        if find_match_at_index(index):
            return index
        else:

            bad_char = haystack[index + needle_length - 1]

            # зсув вправо
            if bad_char in shift_table:
                index += shift_table[bad_char]
            else:
                index += needle_length

    return -1


haystack = "ababcababcabcabc"
needle = "abcabc"
result = boyer_moore_search(haystack, needle)

if result != -1:
    print(f"Стрічка '{needle}' знайдена в стрічці '{haystack}' за індексом {result}.")
else:
    print(f"Стрічка '{needle}' не знайдена в стрічці '{haystack}'.")
