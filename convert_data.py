import json
import uuid
from datetime import datetime, timezone
import sys

def main():
    # 1. 从标准输入加载原始数据
    try:
        raw_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"错误：无法解析输入的 JSON 数据。{e}", file=sys.stderr)
        sys.exit(1)
    
    # 2. 转换数据格式
    sites = []
    api_sites = raw_data.get('api_site', {})
    
    for key, site_info in api_sites.items():
        # 检查名称是否包含🔞符号
        site_name = site_info.get('name', '')
        
        # 根据是否包含🔞符号设置不同的tags
        if '🔞' in site_name:
            tags = ["成人"]
        else:
            tags = ["优秀"]
        
        # 为目标格式的每个站点生成唯一ID
        new_site = {
            "id": str(uuid.uuid4()),
            "key": site_name,  # 使用 name 作为 key
            "name": site_name,
            "api": site_info.get('api', ''),
            "type": 2,
            "isActive": 1,
            "time": datetime.now(timezone.utc).isoformat(),
            "isDefault": 0,
            "remark": f"源站: {key}",
            "tags": tags,  # 使用动态设置的tags
            "priority": 0,
            "proxyMode": "none",
            "customProxy": ""
        }
        sites.append(new_site)
    
    # 3. 构建最终输出的数据结构
    output_data = {
        "sites": sites,
        "exportTime": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
        "total": len(sites),
        "filters": {
            "search": None,
            "tags": None,
            "status": None
        }
    }
    
    # 4. 输出转换后的 JSON 数据
    json.dump(output_data, sys.stdout, indent=2, ensure_ascii=False)
    print()  # 添加换行符，使输出更整洁

if __name__ == "__main__":
    main()
