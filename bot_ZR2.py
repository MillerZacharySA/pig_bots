def choice(round_score, my_score, opponent_score):
  if my_score + round_score > 99 or opponent_score>99:
    return False
  return roll[my_score][opponent_score][round_score]