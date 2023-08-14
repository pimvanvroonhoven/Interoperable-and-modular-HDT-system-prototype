import requests, player_types

url = "https://api3-new.gamebus.eu/v2/players/993/activities?gds=SUGARVITA_PLAYTHROUGH"
payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZ2FtZWJ1c19hcGkiXSwidXNlcl9uYW1lIjoiZC52YW5laWpsQHN0dWRlbnQuZm9udHlzLm5sIiwic2NvcGUiOlsicmVhZCIsIndyaXRlIiwidHJ1c3QiXSwiZXhwIjoxNzY3OTQyODcxLCJhdXRob3JpdGllcyI6WyJERVYiLCJVU0VSIl0sImp0aSI6InQ3OUZnQm4xaGprX3BnSG1CQ0NPOVVXc3BEayIsImNsaWVudF9pZCI6ImdhbWVidXNfYmFzZV9hcHAifQ.Ey9WBijTTCoB5WdmiWb_pfrBOPUHxSh0b8jGlWzPqK3ahTbkGdGvG5alm3Tl75cse3RVSq7Y-XttuoStQSXMJpLTEMjXFCuqEbkp-wvnl-xepguWutGECaFJy0XxlGUTOfBYe8Zahl7sN6TTH3h0aZYw2LD60qHEPdcL3bpeW0NBcq4um_50E-0mHdgtxQWzblVy6fr5itjmI-4azSlr2XOYyamNYNmsjfnfHQPNq1RYhFpy-ewXc7s1svFh9EhOMd5OcWD0ht5cDRcm6Iqz6T06W6az05fIWlXN2Q9k5SzPu0Ct0YBkzr4EXxwXyJeT-nWZnCbi30wYwEd78FtsJw'
  }
response = requests.request("GET", url, headers=headers, data=payload)


if __name__ == "__main__":
    parsed_metrics=player_types.parse_json(response)
    #parsed_metrics=player_types.parse_json_try(response)
    parsed_metrics_cleaned=player_types.remove_nan(parsed_metrics)
    metrics_overview=player_types.manipulate_initial_metrics(parsed_metrics_cleaned)
    metrics_overview_normalized=player_types.normalize_metrics(metrics_overview)
    #print(metrics_overview_normalized)
    player_types_labels=player_types.get_player_types(metrics_overview_normalized)
    print(player_types_labels)