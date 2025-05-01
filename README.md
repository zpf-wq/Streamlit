# 📊 Streamlit 实验记录管理系统

**本项目是一个使用 Streamlit 构建的图形化实验日志管理工具，旨在帮助科研人员记录、上传和查看实验日志、实验结果图像和代码，方便日常科研过程的归档和查阅。**

# 🧩 功能概览

## 1. 🗓 创建实验记录

- 用户可以选择实验日期，自动在 `Logs/`, `Imag/`, `Code/` 目录下创建对应文件夹。

- 支持重复创建日期处理，防止覆盖已有数据。

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/1a53e5a8-f788-4eba-9fa8-576f72e4fcde" />

## 2. 📝 实验日志记录

- 提供 Markdown 风格文本区域供用户记录实验过程、分析或心得。
- 日志自动保存为文本文件：`Logs/<日期>/<日期>.txt`。

## 3. 🖼 上传实验图像

- 支持多张 `.jpg`, `.png`, `.jpeg` 图像上传。

- 显示上传的图像结果。

- 自动保存至：`Imag/<日期>/<日期>_<原图名>.png`。

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/3ac2290a-0443-44b9-a542-045bab6dbb7b" />

## 4. 💻 上传与展示代码

- 支持上传多个 `.py` 脚本。

- 实时在网页中高亮显示代码内容。

- 保存至：`Code/<日期>/<原始文件名>`。

- 自动格式化代码（去除连续空行）。

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/ea9a7ccd-5f43-4524-9199-6b17e26dfef5" />

## 5. ✅ 提交与保存

- 提交后会展示保存进度条，并将上传的图像和代码保存到对应目录。

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/e243c0fe-9428-442b-b6ad-6d81c2dc378e" />

## 6. 🔎 实验日志搜索

- 可按日期精准搜索日志。

- 支持“批量查阅”：以选定日期为中心，显示其前后三天的实验记录。

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/bf4bd9dd-5b05-4908-a120-e34e79bc090d" />

## 7. 📂 浏览所有历史日志

- 以展开列表形式展示所有记录，包括日志文本、图像结果和代码。

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/cc7d276f-7431-428c-a1ec-fe752f813b2d" />

  <img width="1304" alt="image" src="https://github.com/user-attachments/assets/c60e23d2-ac94-4e48-a6d7-e4ed3298f7d7" />

## 8. 🌐 ngrok 外网访问
- 一键生成公网访问链接，便于远程使用
- ngrok官网注册专属令牌
  ````c
  Windows:
  ngrok config add-authtoken 专属令牌
  MacOS:
  ngrok authtoken 专属令牌
  ````
- 通过本地端口号实登录
  ````c
  ngrok http http://localhost:端口号
  ````

  <img width="311" alt="image" src="https://github.com/user-attachments/assets/d2e29ec7-1411-40e5-9296-33b721c90a37" />
