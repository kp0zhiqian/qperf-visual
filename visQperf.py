import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class PerfData:
    def __init__(self):
        self.tcp_bw_list = []
        self.udp_bw_list = []
        self.tcp_lat_list = []
        self.udp_lat_list = []
        self.msg_size_list = []

    def _mbps_to_gbps(self, mbps):
        return float(mbps)/1000
    
    def _fmt_msg_size(self, size):
        if size == 'bytes':
            return 'B'
        else:
            return 'KB'

    def get_list(self, list_name):
        def get_tcp_bw(self):
            r = []
            for i in self.tcp_bw_list:
                r.append(i['bw'])
            return r
        def get_tcp_lat(self):
            r = []
            for i in self.tcp_lat_list:
                r.append(i['lat'])
            return r
        def get_udp_bw(self):
            r = []
            for i in self.udp_bw_list:
                r.append(i['bw'])
            return r
        def get_udp_lat(self):
            r = []
            for i in self.udp_lat_list:
                r.append(i['lat'])
            return r

        list_match = {
            'tcp_bw_list': get_tcp_bw,
            'udp_bw_list': get_udp_bw,
            'tcp_lat_list': get_tcp_lat,
            'udp_lat_list': get_udp_lat
        }

        method = list_match.get(list_name)
        return method(self)


    def read_tcp_bw(self, file_path):
        with open(file_path, 'r') as f:
            raw_list = f.readlines()
            item = {}
            for i in raw_list:
                if 'tcp_bw' in i:
                    if item == {}:
                        pass
                    else:
                        item = {}
                else:
                    if i.split()[0] == 'bw':
                        if i.split()[3] == 'Mb/sec':
                            item['bw'] = self._mbps_to_gbps(i.split()[2])
                        else:
                            item['bw'] = float(i.split()[2])
                    elif i.split()[0] == 'msg_size':
                        item['msg_size'] = i.split()[2]+self._fmt_msg_size(i.split()[3])
                        self.msg_size_list.append(i.split()[2]+self._fmt_msg_size(i.split()[3]))
                    elif i.split()[0] == 'time':
                        item['time'] = i.split()[2]
                    elif i.split()[0] == 'timeout':
                        item['timeout'] = i.split()[2]
                        self.tcp_bw_list.append(item)
    def read_udp_bw(self, file_path):
        with open(file_path, 'r') as f:
            raw_list = f.readlines()
            item = {}
            for i in raw_list:
                if 'udp_bw' in i:
                    if item == {}:
                        pass
                    else:
                        item = {}
                else:
                    if i.split()[0] == 'recv_bw':
                        if i.split()[3] == 'Mb/sec':
                            item['bw'] = self._mbps_to_gbps(i.split()[2])
                        else:
                            item['bw'] = float(i.split()[2])
                    elif i.split()[0] == 'msg_size':
                        item['msg_size'] = i.split()[2]+self._fmt_msg_size(i.split()[3])
                        # self.msg_size_list.append(i.split()[2]+self._fmt_msg_size(i.split()[3]))
                    elif i.split()[0] == 'time':
                        item['time'] = i.split()[2]
                    elif i.split()[0] == 'timeout':
                        item['timeout'] = i.split()[2]
                        self.udp_bw_list.append(item)
    def read_tcp_lat(self, file_path):
        with open(file_path, 'r') as f:
            raw_list = f.readlines()
            item = {}
            for i in raw_list:
                if 'tcp_lat' in i:
                    if item == {}:
                        pass
                    else:
                        item = {}
                else:
                    if i.split()[0] == 'latency':
                            item['lat'] = float(i.split()[2])
                    elif i.split()[0] == 'msg_size':
                        item['msg_size'] = i.split()[2]+self._fmt_msg_size(i.split()[3])
                        # self.msg_size_list.append(i.split()[2]+self._fmt_msg_size(i.split()[3]))
                    elif i.split()[0] == 'time':
                        item['time'] = i.split()[2]
                    elif i.split()[0] == 'timeout':
                        item['timeout'] = i.split()[2]
                        self.tcp_lat_list.append(item)
    def read_udp_lat(self, file_path):
        with open(file_path, 'r') as f:
            raw_list = f.readlines()
            item = {}
            for i in raw_list:
                if 'udp_lat' in i:
                    if item == {}:
                        pass
                    else:
                        item = {}
                else:
                    if i.split()[0] == 'latency':
                            item['lat'] = float(i.split()[2])
                    elif i.split()[0] == 'msg_size':
                        item['msg_size'] = i.split()[2]+self._fmt_msg_size(i.split()[3])
                        # self.msg_size_list.append(i.split()[2]+self._fmt_msg_size(i.split()[3]))
                    elif i.split()[0] == 'time':
                        item['time'] = i.split()[2]
                    elif i.split()[0] == 'timeout':
                        item['timeout'] = i.split()[2]
                        self.udp_lat_list.append(item)
        
class CompareChartData:
    def __init__(self):
        self.title = ''
        self.x_axis_label = ''
        self.y_axis_label = ''
        self.x_data_a = []
        self.x_data_b = []
        self.x_data_a_label = ''
        self.x_data_b_label = ''
        self.y_data = []
        self.output_name = ''
    
    def draw_chart(self):
        
        y = np.arange(len(self.y_data))
        width = 0.4

        fig, ax = plt.subplots()
        ax.set_title(self.title)
        plt.grid()
        ax.bar_label(ax.barh(y - width/2, self.x_data_a, width, label=self.x_data_a_label))
        ax.bar_label(ax.barh(y + width/2, self.x_data_b, width, label=self.x_data_b_label))
        ax.set_xticks([x for x in range(int(max(self.x_data_a))) if x % 5 == 0])

        ax.set_ylabel(self.y_axis_label)
        ax.set_xlabel(self.x_axis_label)
        ax.set_yticks(y)
        ax.set_yticklabels(self.y_data)
        ax.legend()

        fig.set_figheight(7)
        fig.set_figwidth(15)
        ax.set_axisbelow(True)
        plt.savefig(self.output_name, bbox_inches='tight')
        


if __name__ == '__main__':
    perf = PerfData()
    perf.read_tcp_bw('tcp_bw.log')
    perf.read_udp_bw('udp_bw.log')
    perf.read_tcp_lat('tcp_lat.log')
    perf.read_udp_lat('udp_lat.log')

    compare1 = CompareChartData()
    compare1.title = 'Bandwidth Compare'
    compare1.x_axis_label = 'Gbp/s'
    compare1.y_axis_label = 'Msg Size'
    compare1.x_data_a = perf.get_list('tcp_bw_list')
    compare1.x_data_b = perf.get_list('udp_bw_list')
    compare1.x_data_a_label = 'TCP BW'
    compare1.x_data_b_label = 'UDP BW'
    compare1.y_data = perf.msg_size_list
    compare1.output_name = 'Bandwidth.png'
    compare1.draw_chart()

    compare1 = CompareChartData()
    compare1.title = 'Latency Compare'
    compare1.x_axis_label = 'us'
    compare1.y_axis_label = 'Msg Size'
    compare1.x_data_a = perf.get_list('tcp_lat_list')
    compare1.x_data_b = perf.get_list('udp_lat_list')
    compare1.x_data_a_label = 'TCP Lat'
    compare1.x_data_b_label = 'UDP Lat'
    compare1.y_data = perf.msg_size_list
    compare1.output_name = 'Latency.png'
    compare1.draw_chart()

    
    


