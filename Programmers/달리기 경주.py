def solution(players, callings):
    players_idx = {player: i for i, player in enumerate(players)}
    for call in callings:
        idx = players_idx[call]
        players[idx-1], players[idx] = players[idx], players[idx-1]
        players_idx[players[idx-1]] = idx - 1
        players_idx[players[idx]] = idx

    return players
