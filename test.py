seed_matrix = [[7, 3, 1, 4, 2025],
               [2, 1, 1, 5, 2026]]

new_matrix = [row[len(seed_matrix[0])-2:] for row in seed_matrix]
print(new_matrix)
