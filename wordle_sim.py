import statistics

from gamestate import GameState


def play_round(answer):
    gamestate = GameState(verbose=False, use_entropy=False, answer=answer)
    while not gamestate.solved:
        gamestate.guess()
    return gamestate.turns


if __name__ == "__main__":
    with open('actual_words.txt', 'r') as f:
        answers = [x.strip() for x in f.readlines()]

    totes = [play_round(x) for x in answers]

    print(f'bot is winning in an average of {statistics.mean(totes)} turns, with a std dev of {statistics.stdev(totes)} turns')
