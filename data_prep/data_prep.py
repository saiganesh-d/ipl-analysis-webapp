import sqlite3
import csv


def create_tables(conn):
    cur = conn.cursor()

    cur.execute("DROP TABLE Matches")
    cur.execute("DROP TABLE Deliveries")

    query = """CREATE TABLE Matches(
id INTEGER,
season INTEGER,
city VARCHAR(50),
date DATE,
team1 VARCHAR(100),
team2 VARCHAR(100),
toss_winner VARCHAR(100),
toss_decision VARCHAR(20),
result VARCHAR(50),
dl_applied INTEGER,
winner VARCHAR(100),
win_by_runs INTEGER,
win_by_wickets INTEGER,
player_of_match VARCHAR(150),
venue VARCHAR(150),
umpire1 VARCHAR(150),
umpire2 VARCHAR(150),
umpire3 VARCHAR(150)
)
    """
    cur.execute(query)

    query = """CREATE  TABLE Deliveries(
match_id INTEGER,
inning INTEGER,
batting_team VARCHAR(150),
bowling_team VARCHAR(150),
over INTEGER,
ball INTEGER,
batsman VARCHAR(150),
non_striker VARCHAR(150),
bowler VARCHAR(150),
is_super_over INTEGER,
wide_runs INTEGER,
bye_runs INTEGER,
legbye_runs INTEGER,
noball_runs INTEGER,
penalty_runs INTEGER,
batsman_runs INTEGER,
extra_runs INTEGER,
total_runs INTEGER,
player_dismissed VARCHAR(150),
dismissal_kind VARCHAR(150),
fielder VARCHAR(150)
)
    """
    cur.execute(query)
    cur.close()
    print("Tables Created")


def load_matches(conn):
    cur = conn.cursor()

    with open('/Users/nkommoju/Downloads/ipl_data/matches.csv', 'r') as f:
        dr = csv.DictReader(f) 
        to_db = [
            (i['id'], i['season'], i['city'], i['date'], i['team1'], i['team2'], i['toss_winner'], i['toss_decision'],
             i['result'], i['dl_applied'], i['winner'], i['win_by_runs'], i['win_by_wickets'], i['player_of_match'],
             i['venue'], i['umpire1'], i['umpire2'], i['umpire3']) for i in dr]

    cur.executemany(
        "INSERT INTO Matches (id, season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2, umpire3) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()

    cur.execute("SELECT * FROM Matches LIMIT 10")
    for row in cur.fetchall():
        print(row)


def load_deliveries(conn):

    cur = conn.cursor()

    with open('deliveries.csv', 'r') as f:
        dr = csv.DictReader(f)
        to_db = [
            (i['match_id'], i['inning'], i['batting_team'], i['bowling_team'], i['over'], i['ball'], i['batsman'],
             i['non_striker'],
             i['bowler'], i['is_super_over'], i['wide_runs'], i['bye_runs'], i['legbye_runs'], i['noball_runs'],
             i['penalty_runs'], i['batsman_runs'], i['extra_runs'], i['total_runs'],
             i['player_dismissed'], i['dismissal_kind'], i['fielder']) for i in dr]

    cur.executemany(
        "INSERT INTO Deliveries (match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()

    cur.execute("SELECT * FROM Deliveries LIMIT 10")
    for row in cur.fetchall():
        print(row)


def graph_1(conn):
    query = "SELECT season, COUNT(1) No_of_matches FROM Matches GROUP BY season ORDER BY season"
    cur = conn.cursor()

    cur.execute(query)
    for row in cur.fetchall():
        print(row)


def main():
    con = sqlite3.connect("/Users/nkommoju/Learnings/googlecharts_django-master/googlecharts_project/db.sqlite3")
    create_tables(con)
    load_matches(con)
    load_deliveries(con)


    con.close()


if __name__ == '__main__':
    main()
