# 📺 TVBox 影视源配置自动合并 (Auto-Merge Config)

[![Update JSON Config](https://github.com/JE668/LunaTV-config-to-OmniBox-config/actions/workflows/update_json.yml/badge.svg)](https://github.com/JE668/LunaTV-config-to-OmniBox-config/actions/workflows/update_json.yml)

本项目利用 **GitHub Actions** 每天自动拉取、转换、去重并合并影视配置接口数据，生成适用于 OmniBox 等影视软件的标准 JSON 订阅文件。

## ✨ 项目特性

1.  **多源合并**：自动从多个上游仓库拉取 JSON 配置。
2.  **格式转换**：将 `jingjian.json` 的字典格式自动转换为列表格式（适配 OmniBox 标准）。
3.  **智能去重**：
    *   以 `baseUrl`（API 地址）为去重标准。
    *   **保留策略**：若数据重复，严格保留基准文件 (`test.json`) 中的配置，忽略新转换的数据。
4.  **自动排序**：自动识别现有数据的最大 `priority`（优先级），并为新加入的源自动生成递增的优先级序号。
5.  **定时更新**：每天北京时间早上 08:00 自动运行，保持数据最新。

## 🛠️ 数据处理逻辑

脚本 (`process.py`) 按照以下逻辑处理数据：

### 数据源
*   **基准数据 (Primary)**: [jingjian.json](https://raw.githubusercontent.com/hafrey1/LunaTV-config/refs/heads/main/jingjian.json)
    *   *作为主库，所有数据均保留。*


## 🚀 使用方法

### 获取订阅链接
合并后的文件名为 `converted_data.json`。你可以直接在电视盒子或影视 APP 中使用以下链接：

```text
https://gh.llkk.cc/https://github.com/JE668/LunaTV-config-to-OmniBox-config/blob/main/converted_data.json
