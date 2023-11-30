# fastapi-deploy-example

## 项目构建
```bash
poetry init
poetry source add --priority=default aliyun http://mirrors.cloud.aliyuncs.com/pypi/simple/
echo >> pyproject.toml <<
# pytest
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
EOF
poetry add pytest pytest-cov black fastapi uvicorn pydantic
poetry add -D pyinstaller
```

## pyinstaller 打包
注意要关闭`uvicorn`的reload，和修改`run()`
```py
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=30682, log_level="info", reload=False)
```
开始打包
```bash
pyinstaller -D main.py
```
单文件运行
```bash
./dist/main/main
```
打包的时候会生成一个`main.spec`文件
```py
a = Analysis(
    ['main.py'],
    ...
    datas=[
        ('./config', 'config'),
    ],
    hiddenimports=[],
    ...
)
```
这个文件最重要的两个选项是：

* datas
* hiddenimports

`datas`中配置包内文件夹映射关系，解决自己写的包找不到的问题
`hiddenimports`配置第三方包找不到的问题
