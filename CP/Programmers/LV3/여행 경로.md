def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)
    
    def dfs(city):
        if len(answer) == len(tickets) + 1:
            return True
        for i in range(len(tickets)):
            start, dst = tickets[i]
            if start == city and not visited[i]:
                answer.append(dst)
                visited[i] = True
                if dfs(dst):
                    return True
                visited[i] = False
                answer.pop()
        return False
    
    answer.append("ICN")
    dfs("ICN")
    return answer