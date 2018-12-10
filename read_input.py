from data_types import Endpoint, Server, Video
from main import main


def read_file(name):
    with open(name + '.in') as input_file:
        f = input_file.read().split('\n')
        f = [n.split(" ") for n in f]

    for i in range(len(f)):
        f[i] = [int(n) for n in f[i]]

    info = {"videos": f[0][0], "endpoints": f[0][1], "request_d": f[
        0][2], "caches": f[0][3], "cache_size": f[0][4]}
    endpoints = [Endpoint(i) for i in range(f[0][1])]
    video_sizes = f[1]
    videos = []
    for i in range(f[0][0]):
        video = Video(i)
        video.size = video_sizes[i]
        videos.append(video)
    servers = []
    for i in range(f[0][3]):
        server = Server(i)
        server.capacity = f[0][4]
        servers.append(server)
    endpoint_info = f[2: len(f) - info["request_d"]]
    step = 0
    my_num = 0
    for i in range(len(endpoint_info)):
        if i == step:
            l, c = endpoint_info[i]
            step += c + 1
            endpoints[my_num].datacenter_latency = l
            for j in range(i + 1, i + c + 1):
                c, l = endpoint_info[j]
                endpoints[my_num].servers.append((c, l))
                servers[c].endpoints.append((i, l))
            my_num += 1

    num_of_requests = 0
    requests = []
    request_info = f[len(f) - info["request_d"]:]

    for index in range(f[0][2]):
        vid, end, num = request_info[index][0], request_info[index][1], request_info[index][2]
        endpoints[end].requests.append((vid, num))
        num_of_requests += num
        requests.append((end, vid, num))

    return main(servers, videos, endpoints, requests, num_of_requests, name, choice)


filenames = ['me_at_the_zoo', 'trending_today', 'videos_worth_spreading', 'kittens']
choice = int(input("Please, choose prefered algorithm\n Type 1 for greedy_sort.py\n Type 2 for "
                       "greedy_next_neighbour\n Type 3 for weighted greedy_sort\n"))
for file in filenames:
    read_file(file)
