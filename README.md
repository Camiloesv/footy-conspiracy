# Scandal at the Footy Association

Something is rotten in the state of Australian Rules Football. The official Australian Footy Association ladder has started displaying some bizarre rankings. Historically terrible teams are suddenly climbing to the top of the board, while reigning champions are plummeting.

We suspect a rogue software engineer has been quietly slipping biased logic into our automated ranking systems. She wants her team to always win! She thinks she can hide her footprints in complex Python files, but we have a team of Code Detectives on the case.

## Your Mission: Crack the Conspiracy

You will be split into breakout groups. Each group is assigned to investigate one of five suspicious Pull Requests targeting our ranking algorithm.

> **Group Mission**
> Your team must uncover the conspiracy hidden in your assigned PR and present your findings to the class. Expose the rogue employee!

## How to run the code

```bash
python run_season.py
```

This prints the league ladder using the algorithm in `ranking.py`. Try running it on `main` first to see the "honest" ladder, then check out the PR branch your group has been assigned and run it again. What changed? Who benefits?

## Investigation Protocol

Don't let syntax scare you. Look at the variable names, conditional blocks (`if`), and mathematical operators. Work with your group to answer these core questions:

1. **What is the code actually doing?** Translate the suspicious lines into plain English.
2. **Who benefits from this change?** Identify which team gets an unfair boost.
3. **What are the real-world consequences?** What happens to the ladder by the end of the season?

Prepare a quick 1-to-2 minute brief to present your findings to the rest of the commission.

## Files

| File           | What it does                                                    |
| -------------- | --------------------------------------------------------------- |
| `ranking.py`   | The ranking algorithm. **This is where the sabotage hides.**    |
| `teams.py`     | List of teams in the league.                                    |
| `matches.py`   | Sample season results.                                          |
| `run_season.py`| Runs the algorithm and prints the ladder.                       |
