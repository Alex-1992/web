import os
import re


def kill_process(port):
    ret = os.popen("netstat -nao|findstr " + str(port))
    # 注意解码方式和cmd要相同，即为"gbk"，否则输出乱码
    str_list = ret.read().decode('gbk')

    ret_list = re.split('', str_list)
    try:
        process_pid = list(ret_list[0].split())[-1]
        os.popen('taskkill /pid ' + str(process_pid) + ' /F')
        print('端口已被释放')
    except:
        print('端口未被使用')


def killport(port):
    command = '''kill -9 $(netstat -nlp | grep :'''+str(port) + \
        ''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
    os.system(command)


if __name__ == '__main__':
    killport(9000)
