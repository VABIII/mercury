from services.signal_services import fetch_signal_event_data
from services.tivoli_services import fetch_tivoli_event_data
import asyncio


if __name__ == '__main__':
    print("Hello World")
    # asyncio.run(fetch_signal_event_data())
    asyncio.run(fetch_tivoli_event_data())
    # print("FIN")





# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# [x*2 for x in vec]
# [-8, -4, 0, 4, 8]
# # filter the list to exclude negative numbers
# [x for x in vec if x >= 0]
# [0, 2, 4]
# # apply a function to all the elements
# [abs(x) for x in vec]
# [4, 2, 0, 2, 4]
# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']
# # create a list of 2-tuples like (number, square)
# [(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# # the tuple must be parenthesized, otherwise an error is raised
# [(x, x**2) for x in range(6)]
#   File "<stdin>", line 1
#     [(x, x**2) for x in range(6)]
# # SyntaxError: did you forget parentheses around the comprehension target?
# # flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# [num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]