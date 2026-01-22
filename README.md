# PDF分类工具

## 功能介绍

这是一个用于提取PDF文件中文本框信息并按指定标题分类的工具。主要功能包括：

- 提取PDF文件中指定标题（如"PART#:"）后面的字符
- 按提取的字符对PDF页面进行分类
- 为每个分类创建单独的PDF文件
- 交互式输入分类标题

## 使用方法

### 方法一：使用EXE可执行文件（推荐）

1. 打开 `dist` 目录
2. 双击运行 `extract_part_numbers.exe`
3. 当提示"需要以那个标题分类: "时，输入分类标题（如`PART#:`）并回车
4. 程序会自动处理当前目录中的PDF文件
5. 分类完成后，生成的PDF文件会保存在同一目录中

### 方法二：使用Python脚本

1. 确保已安装Python 3.7+
2. 安装依赖：`pip install pypdf`
3. 运行脚本：`python extract_part_numbers.py`
4. 按照提示输入分类标题

## 工作原理

1. **读取PDF文件**：使用pypdf库读取PDF文件内容
2. **提取信息**：从每个页面提取指定标题后面的字符
3. **分类页面**：按提取的字符对页面进行分组
4. **生成文件**：为每个分组创建单独的PDF文件

## 示例

### 输入输出示例

**输入**：
```
需要以那个标题分类: PART#:
```

**输出**：
```
Using title pattern: 'PART#:'
Found 1 PDF file(s) to process:
  - Wayfair_Carton_Labels_SPOS_19956977_1.pdf

Processing Wayfair_Carton_Labels_SPOS_19956977_1.pdf...
Page 1: PART#: = COT004-25x2-WM
Page 2: PART#: = COT004-25x2-WM
...

Saving 8 pages for PART#: COT004-25x2-WM...
Saved to COT004-25x2-WM.pdf
Saving 20 pages for PART#: COT026-25x2-WM...
Saved to COT026-25x2-WM.pdf
...
```

## 生成的文件

分类完成后，会生成以下类型的文件：

- `[分类值].pdf` - 包含所有对应分类页面的PDF文件

## 技术要求

- **EXE版本**：无需安装任何依赖，直接运行
- **Python脚本版本**：
  - Python 3.7+
  - pypdf库

## 注意事项

1. 工具会自动识别并只处理原始PDF文件，避免重复处理
2. 如果PDF文件中没有找到指定标题，对应页面会被标记为"No [标题] found"
3. 生成的文件名基于提取的分类值，请确保分类值适合作为文件名

## 常见问题

### Q: 工具支持哪些PDF文件格式？
A: 支持标准的PDF文件格式，包括文本可提取的PDF文件。

### Q: 分类标题区分大小写吗？
A: 是的，分类标题区分大小写，请确保输入的标题与PDF文件中的实际标题完全一致。

### Q: 如果PDF文件很大，处理时间会很长吗？
A: 是的，处理时间取决于PDF文件的大小和页数。对于大型PDF文件，请耐心等待。

## 联系方式

如有任何问题或建议，请联系开发人员。

---

*版本：1.0.0*
*更新日期：2026-01-22*