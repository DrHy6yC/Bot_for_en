def getLevelUser(balls_percent: float) -> str:
    if balls_percent == 0:
        levelUser = "No level"
    elif 1 <= balls_percent <= 30:
        levelUser = "Beginner (A1)"
    elif 30 < balls_percent <= 60:
        levelUser = "Elementary (A2)"
    elif 60 < balls_percent <= 90:
        levelUser = "Pre-Intermediate (B1)"
    else:
        levelUser = "Intermediate (B2)"
    return levelUser


class Survey:
    pass


if __name__ == '__main__':
    print(getLevelUser(67))
