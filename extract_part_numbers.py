import os
import re
from pypdf import PdfReader, PdfWriter

def extract_part_number(text, title_pattern):
    """从文本中提取指定标题后面的字符"""
    # 转义用户输入的标题，使其可以在正则表达式中使用
    escaped_title = re.escape(title_pattern)
    match = re.search(rf'{escaped_title}\s*(\S+)', text)
    if match:
        return match.group(1)
    return None

def process_pdf(input_pdf, title_pattern):
    """处理PDF文件，提取指定标题后面的字符并分类页面"""
    print(f"Processing {input_pdf}...")
    
    # 读取PDF文件
    reader = PdfReader(input_pdf)
    
    # 按提取的字符分类页面
    part_pages = {}
    
    # 遍历每一页
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        
        # 提取指定标题后面的字符
        part_number = extract_part_number(text, title_pattern)
        
        if part_number:
            print(f"Page {page_num + 1}: {title_pattern} = {part_number}")
            if part_number not in part_pages:
                part_pages[part_number] = []
            part_pages[part_number].append(page_num)
        else:
            print(f"Page {page_num + 1}: No {title_pattern} found")
    
    # 保存分类后的PDF文件
    for part_number, pages in part_pages.items():
        print(f"Saving {len(pages)} pages for {title_pattern} {part_number}...")
        
        # 创建PDF写入器
        writer = PdfWriter()
        
        # 添加页面
        for page_num in pages:
            writer.add_page(reader.pages[page_num])
        
        # 保存文件
        output_pdf = f"{part_number}.pdf"
        with open(output_pdf, 'wb') as f:
            writer.write(f)
        
        print(f"Saved to {output_pdf}")
    
    return part_pages

if __name__ == "__main__":
    # 询问用户分类标题
    title_pattern = input("需要以那个标题分类: ").strip()
    print(f"Using title pattern: '{title_pattern}'")
    
    # 获取当前目录的PDF文件，排除脚本本身和可能的分类结果文件
    pdf_files = []
    for f in os.listdir('.'):
        if f.lower().endswith('.pdf') and f != os.path.basename(__file__):
            # 检查是否可能是分类结果文件（通常是简短的名称，不含下划线等复杂字符）
            # 这里简单判断：如果文件名长度超过50，可能是原始文件
            if len(f) > 50:
                pdf_files.append(f)
    
    # 如果没有找到长文件名的PDF，就处理所有PDF文件
    if not pdf_files:
        pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and f != os.path.basename(__file__)]
    
    print(f"Found {len(pdf_files)} PDF file(s) to process:")
    for f in pdf_files:
        print(f"  - {f}")
    print()
    
    for pdf_file in pdf_files:
        part_pages = process_pdf(pdf_file, title_pattern)
        
        # 打印统计信息
        print(f"\nSummary for {pdf_file}:")
        for part_number, pages in part_pages.items():
            print(f"{title_pattern} {part_number}: {len(pages)} pages")
        print()