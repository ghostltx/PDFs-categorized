import os

# 获取当前目录的PDF文件
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

# 分离原始文件和生成的文件
original_file = 'Wayfair_Carton_Labels_SPOS_19956977_1.pdf'
generated_files = [f for f in pdf_files if f != original_file]

print('Generated PDF files:')
for f in generated_files:
    print(f'  - {f}')

print(f'\nTotal generated files: {len(generated_files)}')
print(f'Original file: {original_file}')
print(f'Total PDF files: {len(pdf_files)}')