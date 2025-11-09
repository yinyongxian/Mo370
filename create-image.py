from PIL import Image, ImageDraw, ImageFont

# 图片尺寸
width, height = 240, 416

# 创建白底黑字的图像（1位像素，"1" 模式）
image = Image.new("1", (width, height), color=1)  # 1 表示白色（背景）

# 加载字体，指定大小（可根据实际情况调整大小）
font_size = 54
try:
    # 可使用系统中已有的中文字体路径
    font = ImageFont.truetype(r"c:\WINDOWS\Fonts\MSYH.TTC", font_size)
except IOError:
    raise Exception("未找到字体文件，请将 SimHei.ttf 放在脚本同目录或指定其他字体路径")

# 要绘制的文字
left_text = "不读书的人"
right_text = "思想就会停止"

# 创建画布
draw = ImageDraw.Draw(image)

# 字之间的间距和起始点
line_spacing = 5
char_height = font_size + line_spacing
start_y = (height - max(len(left_text), len(right_text)) * char_height) // 2

# 左边列起始 x 坐标
left_x = 30
# 右边列起始 x 坐标
right_x = 140

# 画左边列
for i, char in enumerate(left_text):
    y = start_y + i * char_height
    draw.text((left_x, y), char, font=font, fill=0)  # 0 表示黑色文字

# 画右边列
for i, char in enumerate(right_text):
    y = start_y + i * char_height
    draw.text((right_x, y), char, font=font, fill=0)

# 保存为 PNG
image.save("output_bw.jpg")
print("已保存为 output_bw.jpg")
