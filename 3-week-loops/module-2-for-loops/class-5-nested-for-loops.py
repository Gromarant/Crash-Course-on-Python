#----- Given the following code:
# teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#----- Question: What should the next line be to avoid both variables being printed with the same value?
    # Answer: if home_team != away_team:

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print( home_team + ' vs ' + away_team )

# Output: 
    # Dragons vs Wolves
    # Dragons vs Pandas
    # Dragons vs Unicorns
    # Wolves vs Dragons
    # Wolves vs Pandas
    # Wolves vs Unicorns
    # Pandas vs Dragons
    # Pandas vs Wolves
    # Pandas vs Unicorns
    # Unicorns vs Dragons
    # Unicorns vs Wolves
    # Unicorns vs Pandas