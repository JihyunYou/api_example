from IntervalList import IntervalList


def main():
    rl = IntervalList()
    rl.add([1, 5])
    rl.print()
    # Should display: [1, 5)
    rl.add([10, 20])
    rl.print()
    # Should display: [1, 5) [10, 20)
    rl.add([20, 20])
    rl.print()
    # Should display: [1, 5) [10, 20)
    rl.add([20, 21])
    rl.print()
    # Should display: [1, 5) [10, 21)
    rl.add([2, 4])
    rl.print()
    # Should display: [1, 5) [10, 21)
    rl.add([3, 8])
    rl.print()
    # Should display: [1, 8) [10, 21)
    rl.remove([10, 10])
    rl.print()
    # Should display: [1, 8) [10, 21)
    rl.remove([10, 11])
    rl.print()
    # Should display: [1, 8) [11, 21)
    rl.remove([15, 17])
    rl.print()
    # Should display: [1, 8) [11, 15) [17, 21)
    rl.remove([3, 19])
    rl.print()
    # Should display: [1, 3) [19, 21)

    ra = IntervalList()
    ra.add([1, 5])
    rb = IntervalList()
    rb.add([1, 6])

    print(ra > rb)
    # Should display: false
    print(ra < rb)
    # Should display: true
    ra.add([7, 8])
    rb.add([7, 9])
    print(ra >= rb)
    # Should display: false
    print(ra <= rb)
    # Should display: true
    print(ra == rb)
    # Should display: false
    print(ra in rb)
    # Should display: true


if __name__ == "__main__":
    main()


