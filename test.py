def perform_moves(A, B, num_moves):
    for i in range(num_moves):
        if not B:
            print("List B is empty. Cannot perform further moves.")
            break

        current_moves = B[-1]  # Get the last element from list B
        next_steps = []

        for move in current_moves:
            if move < len(A):
                next_steps.extend(A[move - 1])  # Adjust index to match list A (0-based index)

        if next_steps:
            B.append(next_steps)  # Add the next step(s) to list B
            print(f"Move {i + 1}: Next step for {current_moves} is {next_steps}. Updated list B: {B}")
        else:
            print(f"Move {i + 1}: No valid next step for {current_moves}. Updated list B: {B}")

# List A containing the next steps
A = [[1], [2, 3], [4], [1], [2]]

# List B containing the initial step
B = [[2]]  # Initial step as a list of lists

# Perform 10 moves
perform_moves(A, B, num_moves=10)
