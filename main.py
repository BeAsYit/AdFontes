from write_output import write_file

def main(servers, videos, endpoints, requests, num_of_requests, file_name, algorithm):
    if algorithm == 1:
        from greedy_sort import request_importance, place_video
    if algorithm == 2:
        from greedy_next_neighbour import request_importance, place_video
    if algorithm == 3:
        from weighted_greedy_sort import request_importance, place_video

    def latency_sort(n):
        return n[1]

    def request_importance_sort(n):
        return request_importance(n, videos, endpoints)

    requests.sort(key=request_importance_sort, reverse=True)
    for endpoint in endpoints:
        endpoint.servers.sort(key=latency_sort)

    count = 0
    for item in requests:
        endpoint, video, number = item[0],item[1], item[2]
        place_video(endpoint, video, number, endpoints, videos, servers)
        count += 1

    def calculate_score():
        total = 0
        count = 0
        for endpoint in endpoints:
            count += 1
            for request in endpoint.requests:
                quantity = request[1]
                video = request[0]
                current_min = endpoint.datacenter_latency * quantity
                for i in endpoint.servers:
                    server = servers[i[0]]
                    if video not in server.videos:
                        continue
                    current_min = min(current_min, quantity * i[1])
                total += endpoint.datacenter_latency * quantity - current_min
        return (total / num_of_requests) * 1000
    print(calculate_score())
    write_file(servers, file_name)
