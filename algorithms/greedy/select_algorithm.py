from algorithms.greedy.union_find import union_find
from algorithms.greedy.union_by_rank import union_by_rank
from algorithms.greedy.kurskals_mst import kruskal_mst
from algorithms.greedy.huffman_coding import huffman_coding


def select_greedy_algorithm():
    print("Select Greedy Algorithm")
    print("1. Union Find")
    print("2. Union by Rank")
    print("3. Kruskal's MST")
    print("4. Huffman Coding")

    algorithm = input("Enter Algorithm : ")

    if int(algorithm) == 1:
        union_find()

    elif int(algorithm) == 2:
        union_by_rank()

    elif int(algorithm) == 3:
        kruskal_mst()

    elif int(algorithm) == 4:
        huffman_coding()
