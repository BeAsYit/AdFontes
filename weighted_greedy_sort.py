size_const = 0.13
lat_const = 15


def request_importance(n, videos, endpoints):
    video = videos[n[1]]
    endpoint = endpoints[n[0]]
    return (n[2] * endpoint.datacenter_latency ** lat_const) / video.size ** size_const


def place_video(endpoint, video, quantity, endpoints, videos, servers):
    endpoint = endpoints[endpoint]
    video = videos[video]

    for server in endpoint.servers:
        server = servers[server[0]]

        if video.index in server.videos:
            return

        if server.capacity < video.size:
            continue

        server.capacity -= video.size
        server.videos.append(video.index)
        return
