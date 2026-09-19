import numpy as np


def create_map(rows=8, cols=12, obstacle_probability=0.25):
    return np.random.choice(
        [0, 1],
        size=(rows, cols),
        p=[1 - obstacle_probability, obstacle_probability]
    )


def insert_pattern(game_map, pattern, row, col):
    height, width = pattern.shape
    game_map[row:row + height, col:col + width] = pattern


def find_pattern(game_map, pattern):
    windows = np.lib.stride_tricks.sliding_window_view(
        game_map,
        pattern.shape
    )

    matches = np.all(windows == pattern, axis=(2, 3))

    rows, cols = np.where(matches)

    return [(int(row), int(col)) for row, col in zip(rows, cols)]


def mark_patterns(game_map, pattern, positions):
    result = game_map.copy()

    height, width = pattern.shape

    for row, col in positions:
        result[row:row + height, col:col + width] = 2

    return result


def print_map(game_map):
    for row in game_map:
        print(" ".join(map(str, row)))


def main():
    game_map = create_map()

    pattern = np.array([
        [1, 0],
        [1, 1]
    ])

    insert_pattern(game_map, pattern, 1, 3)
    insert_pattern(game_map, pattern, 5, 8)

    print("Исходная карта:")
    print_map(game_map)

    positions = find_pattern(game_map, pattern)

    print("\nНайденные координаты:")
    for position in positions:
        print(position)

    result = mark_patterns(game_map, pattern, positions)

    print("\nКарта с найденными метками:")
    print_map(result)


if __name__ == "__main__":
    main()
