class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise ValueError("Not enough scores")

            # Get last two scores using negative indexing
            last_two = self.scores[-2:]
            highest = max(last_two)
            print(f"Highest score among last two is: {highest}")
        except ValueError:
            print("Not enough scores to find highest value")


# Example usage
scores = [45, 67, 89, 72]
student = StudentScores(scores)
student.highest_last_two()
