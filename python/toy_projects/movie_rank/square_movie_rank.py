#movie rank implementation practice 
import pytest

RANK_TO_SCORE = {
    1: 3,
    2: 2,
    3: 1
}

def calculate_this_round(round_num, ballot, scoreboard):
    for rank, movie_name in enumerate(ballot, 1):
        if movie_name not in scoreboard:
            scoreboard[movie_name] = 0

        if rank in RANK_TO_SCORE:
            scoreboard[movie_name] += RANK_TO_SCORE[rank]

def calculate_scores(ballots):
    scoreboard = dict()

    for round_num, ballot in enumerate(ballots, 1):
        calculate_this_round(round_num, ballot, scoreboard)

    return scoreboard

def get_rank_from_scoreboard(scoreboard):
    sorted_scoreboard = sorted(
        scoreboard.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return [item[0] for item in sorted_scoreboard]

def check_if_the_winner_can_be_decided_in_early_round(ballots):
    scoreboard = dict()
    total_round = len(ballots)

    for current_round, ballot in enumerate(ballots, 1):
        calculate_this_round(current_round, ballot, scoreboard)
        rank_list = get_rank_from_scoreboard(scoreboard)
        diff_between_first_and_second_player = \
            scoreboard[rank_list[0]] - scoreboard[rank_list[1]]
        if diff_between_first_and_second_player \
            > scoreboard[rank_list[1]]+(3*(total_round-current_round-1)):
            return (True, current_round)
    return (False, -1)


def test_case1():
    ballots = [
        ["A", "B", "C", "D"],
        ["A", "B", "C", "D"],
        ["D", "C", "B", "A"]
    ]
    expected_ans = {
        "A": 6, "B": 5, "C": 4, "D": 3
    }
    ans = calculate_scores(ballots)
    assert expected_ans == ans

def test_case2():
    ballots = [
        ["A", "B", "C", "D", 'E'],
        ["A", "B", "C", "D", 'E'],
        ["C", "B", "D", "E", "A"]
    ]

    expected_ans = {
        "A": 6, "B": 6, "C": 5, "D": 1, "E": 0
    }

    ans = calculate_scores(ballots)
    assert expected_ans == ans

def test_case3():
    ballots = [
        ["C", "B", "A", "D", 'E'],
        ["D", "B", "C", "A", 'E'],
        ["C", "B", "D", "E", "A"]
    ]

    expected_ans = {
        "A": 1, "B": 6, "C": 7, "D": 4, "E": 0
    }

    ans = calculate_scores(ballots)
    assert expected_ans == ans

def test_case4():
    ballots = [
        ["C", "B", "A", "D", 'E'],
        ["D", "B", "C", "A", 'E'],
        ["C", "B", "D", "E", "A"]
    ]
    expected_ans = ["C", "B", "D", "A", "E"]
    scoreboard = calculate_scores(ballots)
    ans = get_rank_from_scoreboard(scoreboard)
    assert expected_ans == ans

def test_case5():
    # if the score of first player > the difference between first and second * rounds
    ballots = [
        ["A", "C", "B", "D", 'E'], # A = 3  C = 2
        ["A", "D", "B", "C", 'E'], # A = 6  C = 2 B = 2 D = 2   A is the winner
        ["A", "E", "D", "B", "A"]
    ]
    expected_ans = (True, 2)
    ans = check_if_the_winner_can_be_decided_in_early_round(ballots)
    assert expected_ans == ans

if __name__ == "__main__":
    pytest.main(["-vv"])
