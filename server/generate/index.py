# 定义普通方法,组织业务

import json

from jinja2 import Template



def codeParse(list,config):
    try:
        template = Template(config.get('content'))
        data = {}
        if config.get('configData'):
            data = json.loads(config.get('configData'))
        
        render = template.render(data)
        return  render
    except Exception as e:
        return e.message   
    

# 使用reder解析
# def parseRender(key, config: Config):
#     res = {}
#     basePath = os.path.join(os.getcwd(), "static", "模板" + key)
#     modelName = config.name.capitalize()
#     for path in list:
#         template = jinjaEngine.get_template(path)
#         content = template.render(config=config)
#         # file = template.stream(content)

#         fileName = path.split("/")[-1]
#         folder = path.replace(fileName, "", 1)
#         path = path.replace(fileName, modelName + fileName, 1)
#         path = path.replace(fileName, modelName + fileName, 1)

#         targetFolder = os.path.join(basePath, config.name, folder)
#         target = os.path.join(basePath, config.name, path)
#         if not os.path.exists(targetFolder):
#             os.makedirs(targetFolder)
#         with open(target, "w", encoding="utf-8") as file:
#             file.write(content)  # 写入模板 生成html

#     # 压缩
#     name = "模板" + key
#     Common.zipfile(
#         os.path.join(os.getcwd(), "static", name),
#         os.path.join(os.getcwd(), "static", name),
#     )
#     res[path] = content
#     return res
