# 企赢 Qiying

面向初创企业的后台运营中心。品牌是「企赢」，日常交互助理是「小赢」。

- [系统原型](https://jiangnan0707.github.io/qiying/)：日常办公、后台办理、老板经营；用报销与入职贯通流程中心、单据中心和台账中心。
- [产品方案与发布演示](https://jiangnan0707.github.io/qiying/plan.html)
- [直接阅读方案路线](https://jiangnan0707.github.io/qiying/plan.html#plan)

## 内容维护

日常编辑这两份源文件：

- `企赢-系统原型.html`
- `企赢-产品方案与演示.html`

修改源文件后，运行下面的发布准备命令，再把变更提交到 `main`。GitHub Pages 会自动将 `docs` 目录发布到上面的固定网址。发布准备时自动转换页面文件名和相互链接，源文件继续保留中文名称。

本地检查发布文件：

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --directory docs
```

然后访问 `http://localhost:8000/`。

## 演示范围

页面内数据与办理记录均为样例；交互进度仅保存在访问者当前浏览器中，不在访问者之间共享。语音、AI、税务、银行、合同签署与会计等外部服务尚未接入。

本仓库为公开演示项目，维护时只使用虚构或已脱敏资料。
