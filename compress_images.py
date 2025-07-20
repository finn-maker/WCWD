#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片压缩脚本
使用 Pillow 库压缩 PNG 图片
"""

import os
from PIL import Image
import glob

def compress_image(input_path, output_path, quality=85):
    """压缩单张图片"""
    try:
        # 打开图片
        with Image.open(input_path) as img:
            # 转换为 RGB 模式（如果需要）
            if img.mode in ('RGBA', 'LA'):
                # 创建白色背景
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # 保存压缩后的图片
            img.save(output_path, 'PNG', optimize=True, quality=quality)
            
            # 获取文件大小
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            print(f"压缩完成: {os.path.basename(input_path)}")
            print(f"  原始大小: {original_size / 1024:.1f} KB")
            print(f"  压缩后: {compressed_size / 1024:.1f} KB")
            print(f"  压缩率: {compression_ratio:.1f}%")
            print()
            
    except Exception as e:
        print(f"压缩失败 {input_path}: {e}")

def main():
    # 输入和输出目录
    input_dir = "src/static/appleFace"
    output_dir = "src/static/appleFace_compressed"
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取所有 PNG 文件
    png_files = glob.glob(os.path.join(input_dir, "*.png"))
    
    if not png_files:
        print("没有找到 PNG 文件")
        return
    
    print(f"找到 {len(png_files)} 个 PNG 文件")
    print("开始压缩...\n")
    
    # 压缩每个文件
    for png_file in png_files:
        filename = os.path.basename(png_file)
        output_path = os.path.join(output_dir, filename)
        compress_image(png_file, output_path)
    
    print("所有图片压缩完成！")

if __name__ == "__main__":
    main() 