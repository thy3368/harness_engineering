# xlsx2md 使用说明

Excel 转 Markdown 工具，自动清理 NaN 值和 Unnamed 列。

---

## 安装依赖

```bash
# 安装 markitdown
pip install markitdown

# 安装 pandas
pip install pandas
```

---

## 基本用法

```bash
python xlsx2md.py <输入文件.xlsx> [选项]
```

---

## 命令行选项

| 选项 | 说明 |
|------|------|
| `-o, --output` | 指定输出 Markdown 文件路径 |

---

## 使用示例

### 1. 基本转换

```bash
python xlsx2md.py document.xlsx
```

输出：`document.md`

### 2. 指定输出文件

```bash
python xlsx2md.py document.xlsx -o output.md
```

### 3. 处理带空格的路径

```bash
python xlsx2md.py "path/to/my file.xlsx" -o "path/to/output.md"
```

---

## 处理效果

| 原始内容 | 处理后 |
|----------|--------|
| `Unnamed: 0` | 空格 |
| `Unnamed: 1` | 空格 |
| `NaN` | 空字符串 |
| 全空行 | 删除 |

---

## 完整示例

```bash
# 转换技术规格书
python xlsx2md.py \
  "技术平台规范/场景规范层/业务规范/参考材料/消息中心-技术规格书.xlsx" \
  -o "消息中心-技术规格书.md"
```

---

## 注意事项

1. **依赖要求**：确保已安装 `markitdown` 和 `pandas`
2. **文件存在**：输入文件必须存在，否则报错退出
3. **编码**：输出文件使用 UTF-8 编码

---

## 故障排查

| 问题 | 解决方案 |
|------|----------|
| `markitdown: command not found` | 安装 markitdown: `pip install markitdown` |
| `No module named 'pandas'` | 安装 pandas: `pip install pandas` |
| `File not found` | 检查文件路径是否正确 |

---

## 脚本位置

`/Users/hongyaotang/src/harness_engineering/xlsx2md.py`
