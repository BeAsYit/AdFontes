def write_file(servers, file_name):
    def servers_sort(server):
        return server.index
    servers.sort(key=servers_sort)
    with open(file_name+'.out', 'w') as output_file:
        output_file.write(str(len(servers)) + "\n")
        for server in servers:
            output_file.write(str(server.index)+" ")
            for v in server.videos:
                output_file.write(str(v)+" ")
            output_file.write('\n')
