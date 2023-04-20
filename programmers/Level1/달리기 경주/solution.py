# 시간복잡도 실패
def solution(players, callings):
    for calling in callings:
        p_idx = players.index(calling)
        players[p_idx-1:p_idx+1] = [players[p_idx], players[p_idx-1]]
    return players

# Hash로 해결
def solution(players, callings):
    players_dict = {v : k for k,v in enumerate(players)}
    for calling in callings:
        idx = players_dict[calling]
        players_dict[calling],players_dict[players[idx-1]] = idx-1 , idx
        players[idx], players[idx-1] = players[idx-1], players[idx]
        print(players)
        
        print(players_dict)
    return players