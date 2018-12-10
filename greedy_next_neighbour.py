size_const = 0.13
lat_const = 15


def request_importance(n, videos, endpoints):
    video = videos[n[1]]
    endpoint = endpoints[n[0]]
    return (n[2] * endpoint.datacenter_latency ** lat_const) / video.size ** size_const


def place_video(endpoint, video, quantity, endpoints, videos, servers):
    placed = False
    neighbour = False

    endpoint = endpoints[endpoint]
    video = videos[video]

    policeman = 25000
    count = 0

    for server in endpoint.servers:
        server = servers[server[0]]
        if placed and neighbour:
            break
        if placed is False:
            if video in server.videos:
                placed = count
        if neighbour is False:
            if server.capacity >= video.size:
                neighbour = count
        count += 1
    if placed is False and neighbour is False:
        return

    if placed is False:
        if neighbour is False:
            neighbour = -1
        server = servers[neighbour]
        server.capacity -= video.size
        server.videos.append(video.index)
        return

    difference = endpoint.servers[placed][1] - endpoint.servers[neighbour][1]
    if difference * quantity < policeman:
        policeman -= difference * quantity
        return

    server = servers[neighbour]
    server.capacity -= video.size
    server.videos.append(video.index)
    return
