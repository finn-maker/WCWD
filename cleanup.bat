@echo off
echo 正在删除多余的压缩文件夹...
rmdir /s /q "src\static\compressed"
rmdir /s /q "src\static\appleFace_compressed"
echo 清理完成！
pause 