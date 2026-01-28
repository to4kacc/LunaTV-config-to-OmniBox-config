import json
import uuid
from datetime import datetime, timezone
import sys

def main():
    # 1. 从原始URL加载数据
    source_url = "https://raw.githubusercontent.com/hafrey1/LunaTV-config/refs/heads/main/jingjian.json"
    
    # 注意：在实际的 GitHub Actions 中，此步骤将由工作流中的 `curl` 命令完成。
    # 这里我们读取从标准输入传递的数据。
    try:
        raw_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"错误：无法解析输入的 JSON 数据。{e}", file=sys.stderr)
        sys.exit(1)
    
    # 2. 转换数据格式
    sites = []
    api_sites = raw_data.get('api_site', {})
    
    for key, site_info in api_sites.items():
        # 为目标格式的每个站点生成唯一ID
        new_site = {
            "id": str(uuid.uuid4()),
            "key": site_info.get('name', '未命名'),  # 使用 name 作为 key
            "name": site_info.get('name', ''),
            "api": site_info.get('api', ''),
            "type": 2,  # 根据你的要求，默认为 2
            "isActive": 1,  # 根据你的要求，默认为 1
            "time": datetime.now(timezone.utc).isoformat(),  # 当前时间
            "isDefault": 0,  # 根据你的要求，默认为 0
            "remark": f"源站: {key}",  # 用原始键（域名）构建备注
            "tags": ["优秀"],  # 根据你的要求，添加默认标签
            "priority": 0,  # 根据你的要求，默认为 0
            "proxyMode": "none",  # 根据你的要求，默认为 none
            "customProxy": ""  # 根据你的要求，默认为空
        }
        sites.append(new_site)
    
    # 3. 构建最终输出的数据结构
    output_data = {
        "sites": sites,
        "exportTime": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',  # 精确到毫秒的格式
        "total": len(sites),
        "filters": {
            "search": None,
            "tags": None,
            "status": None
        }
    }
    
    # 4. 输出转换后的 JSON 数据
    json.dump(output_data, sys.stdout, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
