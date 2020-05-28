# Harbor 工具

调用 Harbor REST API 的 Harbor 运维管理工具。

```bash
usage: harbor [-h] --host HOST --user USER --password PASSWORD [--version]
              ...

Harbor 管理工具

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit

通用选项:
  --host HOST           主机名
  --user USER, -u USER  用户名
  --password PASSWORD, -p PASSWORD 密码

子命令:
  
    project-list        项目列表
    image-list          镜像列表
    image-retag         重定向镜像
```
