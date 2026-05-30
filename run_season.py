from ranking import calculate_standings
from teams import TEAMS
from matches import MATCHES


def print_ladder(standings):
    print()
    print("AUSTRALIAN FOOTY ASSOCIATION - LADDER")
    print("-" * 50)
    print(f"{'Pos':<4}{'Team':<22}{'Points':>8}{'Diff':>10}")
    print("-" * 50)
    for i, team in enumerate(standings, start=1):
        print(f"{i:<4}{team['name']:<22}{team['points']:>8}{team['diff']:>10}")
    print("-" * 50)


if __name__ == "__main__":
    standings = calculate_standings(MATCHES, TEAMS)
    print_ladder(standings)
