from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# 定义自定义的处理程序


class MyHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    def do_GET(self):
        # 解析URL中的查询参数
        parsed_url = urlparse(self.path)
        print(parsed_url, parsed_url.path)

        query_params = parse_qs(parsed_url.query)

        print(query_params, self.path)

        # 获取名为"param"的查询参数的值
        param_value = query_params.get("param", [None])[0]
        keyword_value = query_params.get("keyword", [None])[0]

        if parsed_url.path == '/':
            # 请求首页，返回index.html文件
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('server/index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            # 设置响应状态码
            self.send_response(200)

            # 设置响应头部
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # 构造响应内容
            response = f'GET request received. Param value: {param_value}, k: {keyword_value}'

            # 发送响应内容
            self.wfile.write(response.encode('utf-8'))

        # # 设置响应状态码
        # self.send_response(200)

        # # 设置响应头部
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()

        # # 构造响应内容
        # response = f'GET request received. Param value: {param_value}, keyword: {keyword_value}'

        # # 发送响应内容
        # self.wfile.write(response.encode('utf-8'))

    # 处理POST请求
    def do_POST(self):
        parsed_url = urlparse(self.path)
        print(parsed_url)

        # 获取POST请求的Content-Length
        content_length = int(self.headers['Content-Length'])

        # 读取请求的body数据
        post_data = self.rfile.read(content_length).decode('utf-8')

        print(post_data)

        if parsed_url.path == '/v1/api':
            # 设置响应状态码
            self.send_response(200)

            # 设置响应头部
            self.send_header('Content-type', 'text/stream')
            self.end_headers()

            # 构造响应内容
            response = post_data

            # 发送响应内容
            self.wfile.write(response.encode('utf-8'))
        else:
            # 设置响应状态码
            self.send_response(200)

            # 设置响应头部
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # 构造响应内容
            response = f'POST request received. Body: {post_data}'

            # 发送响应内容
            self.wfile.write(response.encode('utf-8'))


# 创建HTTP服务器


def run():
    # 服务器地址和端口
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting server... http://localhost:8000')

    try:
        # 启动服务器，一直运行直到中断
        httpd.serve_forever()
    except KeyboardInterrupt:
        # 捕获键盘中断，关闭服务器
        pass

    httpd.server_close()
    print('Server stopped.')


# 运行服务器
if __name__ == '__main__':
    run()


# test code in browser console
"""
fetch('http://localhost:8000/v1/api?keyword=test', {
    method: 'POST', body: JSON.stringify({test: 1000000}), data: "post-data",
}).then(res => res.text()).then(console.log).catch(console.log);
"""
