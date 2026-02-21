class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            if len(self.scores) == 0:
                raise ValueError("No scores available")

            # Get difference between last and first score using indexing
            difference = self.scores[-1] - self.scores[0]
            print(f"Difference between last and first score is: {difference}")
        except ValueError:
            print("No scores available to calculate difference")


# Example usage
scores = [55, 65, 75, 85]
student = StudentPerformance(scores)
student.score_difference()
