from django.shortcuts import render
import json
from ipl_charts.models import Matches, Deliveries
from django.db.models import Count, Sum
from django.db import connection


def get_chart1_data(x_axis_title, y_axis_title):
    data = [[x_axis_title, y_axis_title]]

    matches_by_season = Matches.objects.values('season').annotate(matches=Count('id'))
    for row in matches_by_season:
        data.append([row['season'], row['matches']])

    x_axis_json = json.dumps(x_axis_title)
    y_axis_json = json.dumps(y_axis_title)
    return data, x_axis_json, y_axis_json


def get_chart2_data(x_axis_title, y_axis_title):
    data = []

    matches_by_season = Matches.objects.values('season', 'winner').annotate(matches=Count('id'))
    header = ['Year']
    season_matches = {}

    for row in matches_by_season:
        if row["winner"] and row["winner"] not in header:
            header.append(row["winner"])
        if row["season"] not in season_matches.keys():
            season_matches[row["season"]] = {row["winner"]: row['matches']}
        else:
            season_matches[row["season"]].update({row["winner"]: row['matches']})


    data.append(header)
    for year, d in season_matches.items():
        row = [year]
        for team in header[1:]:
            value = d.get(team, 0)
            row.append(value)
        data.append(row)


    x_axis_json = json.dumps(x_axis_title)
    y_axis_json = json.dumps(y_axis_title)
    return data, x_axis_json, y_axis_json


def home(request):
    x_axis_title = 'Season'
    y_axis_title = 'Matches'
    chart1_data, chart1_x_axis_json, chart1_y_axis_json = get_chart1_data(x_axis_title, y_axis_title)

    chart1_modified_data = json.dumps(chart1_data)  # JSON string corresponding to  chart1_data

    x_axis_title = 'Teams'
    y_axis_title = 'Matches Won'
    chart2_data, chart2_x_axis_json, chart2_y_axis_json = get_chart2_data(x_axis_title, y_axis_title)
    chart2_modified_data = json.dumps(chart2_data)


    return render(request, "home.html",
                  {'chart1_values': chart1_modified_data, 'chart1_h_title': chart1_x_axis_json,
                   'chart1_v_title': chart1_y_axis_json,
                   'chart2_values': chart2_modified_data, 'chart2_h_title': chart2_x_axis_json,
                   'chart2_v_title': chart2_y_axis_json}
                  )


def extra_runs(request):
    if request.method == "GET":
        return render(request,"extra_runs.html")


    x_axis_title = 'Teams'
    y_axis_title = 'ExtraRuns Conceded'
    data = [[x_axis_title, y_axis_title]]

    matches_by_season = Deliveries.objects.values('bowling_team').filter(match_id_id_season=2016).annotate(extra_runs=Sum('extra_runs'))
    print(matches_by_season)
    for row in matches_by_season:
        data.append([row['bowling_team'], row['extra_runs']])

    x_axis_json = json.dumps(x_axis_title)
    y_axis_json = json.dumps(y_axis_title)

    modified_data = json.dumps(data)  

    return render(request, "extra_runs.html", {'values': modified_data, 'h_title': x_axis_json, 'v_title': y_axis_json})


def economic_bowler(request):
    """
    Function responsible for rendering the homepage
    """

    x_axis_title = 'Year'
    y_axis_title = 'Economy'
    data = [[x_axis_title, y_axis_title, {'role': 'annotation'}]]

    cursor = connection.cursor()
    query = """SELECT DISTINCT season, min_economy, bowler
         FROM (
         SELECT season, bowler, economy, MIN(economy) OVER(PARTITION BY season) AS min_economy
         FROM (
         SELECT m.season, d.bowler, (SUM(total_runs) * 1.0) / COUNT(DISTINCT over)  AS economy
         FROM Matches m
         JOIN Deliveries d ON m.id = d.match_id
         GROUP BY m.season, d.bowler
        ) A
         GROUP BY season, bowler
        )B
         WHERE economy = min_economy"""
    cursor.execute(query)
    for row in cursor.fetchall():
        data.append([row[0], row[1], row[2]])


    x_axis_json = json.dumps(x_axis_title)
    y_axis_json = json.dumps(y_axis_title)

    modified_data = json.dumps(data)

    return render(request, "economic_bowler.html",
                  {'values': modified_data, 'h_title': x_axis_json, 'v_title': y_axis_json})
